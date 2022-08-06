from django.urls import path
from . import views

app_name = 'wap'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<str:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
