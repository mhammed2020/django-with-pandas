from django.urls import  path
from .  import views

app_name ='products'
urlpatterns = [
    path('', views.home, name='home'),
        path('add/', views.add_purchase_view, name='add-purchase-view'),
]