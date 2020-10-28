from django.urls import path
from . import views

app_name = 'csvs'

urlpatterns = [
    path('', views.upload_file_view, name='upload-view'),
]