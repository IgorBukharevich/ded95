from django.conf.urls.static import static
from django.urls import path

from conf import settings
from maniapp.views import *

app_name = 'very_well_apps'

urlpatterns = [
    path('', index, name='home'),
    path('table/', view_table, name='table')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
