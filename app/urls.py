from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views
from .views import signup

urlpatterns = [
    path('', views.index, name='index'),
    path('заявки', views.order_list, name='order_list'),
    path('заявка/<int:pk>/', views.order_detail, name='order_detail'),
    path('заявка/создание/', views.order_new, name='order_new'),
    path('register/', signup, name='signup'),
    path('заявка/<int:pk>/редактирование/', views.order_edit, name='order_edit'),
]