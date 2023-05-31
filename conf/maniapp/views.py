import json
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from maniapp.forms import UploadedForm
from maniapp.models import ListJson
from maniapp.models import DocJsonFile


def index(request):
    if request.method == 'POST':
        form = UploadedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Файл добавлен в базу данных!'
            )
            try:
                analiz_json(request.FILES['json_file'])
                messages.success(
                    request,
                    'Данные успешно добавились в таблицу!'
                )
            except:
                messages.error(request, '')
            return HttpResponseRedirect('/')
        else:
            messages.error(
                request,
                'Недопустимые данные!'
            )
    else:
        form = UploadedForm()

    documents = DocJsonFile.objects.all()

    return render(
        request, 'index.html',
        {'documents': documents, 'form': form}
    )


def check_date(date) -> bool:
    """
    Проверка валидности даты в json-файле
    :param date: строка в формате - '2012-06-11_12:00'
    :return: True or False
    """
    # формат даты которую провремяем ключ("data")
    format_date = '%Y-%m-%d_%H:%M'
    try:
        datetime.strptime(date, format_date)
    except:
        return False
    return True


def analiz_json(json_file):
    """
    Обработка данных из JSON-файла, для добавления в базу PostgreSQL
    :param json_file: пусть к файлу из базы данных
    :return:
    """
    # ключи
    key_n = 'name'
    key_d = 'date'
    newdoc = DocJsonFile(json_file=json_file)
    newdoc.save()

    path = newdoc.json_file.path
    with open(path) as file:
        data = json.load(file)

    for val in range(len(data)):
        # получение словаря из списка
        data_dict = data[val]

        # проверка валидности данных в ключ/значение, фильтрация нужных данных
        if (key_n in data_dict and key_d in data_dict) and (
                len(data_dict[key_n]) <= 50) and (
                check_date(data_dict[key_d])
        ):

            name_str = data_dict[key_n]
            date_str = data_dict[key_d].replace('_', ' ')
            if name_str and date_str != '':
                ListJson.objects.create(name=name_str, date=date_str)
            else:
                pass


def view_table(request):
    """
    Отображение табилицы баз данных
    :return: ''
    """
    table_json = ListJson.objects.all()
    return render(request, 'table_view.html', {'json_lists': table_json})
