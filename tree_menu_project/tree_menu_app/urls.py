from django.urls import path
from tree_menu_app import views

urlpatterns = [
    path('', views.index_page, name='index_page_url'),
    path('clothes/', views.clothes_page, name='clothes_page_url'),
    path('clothes/outerwear/', views.outerwear_page)
]