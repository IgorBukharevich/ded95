from django.db import models


class DocJsonFile(models.Model):
    class Meta:
        verbose_name = u'JSON-файл'
        verbose_name_plural = u'JSON-файлы'

    json_file = models.FileField(
        verbose_name=u'JSON-файл',
        upload_to='files/',
        null=True,
    )

    def __repr__(self):
        return self.json_file

    def __str__(self):
        return self.json_file


class ListJson(models.Model):
    """Модель базы данных - Таблица 'ListJson'"""

    class Meta:
        verbose_name = u'База из JSON'
        verbose_name_plural = u'Базы из JSON'

    name = models.CharField(
        verbose_name=u'Имя',
        max_length=50,
    )

    date = models.DateTimeField(
        verbose_name=u'Дата/Время',
    )

    def __str__(self):
        return self.name, self.date
