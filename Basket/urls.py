from django.urls import path

from . import views

app_name = 'Basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),
    path('delete/', views.basket_delete, name='basket_delete'),
    path('update/', views.basket_update, name='basket_update'),
    path('sendData/', views.sendData, name="sendData"),
]
