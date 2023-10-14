from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.API_View, name='apiTest'),
    path('api/v1/<int:id>/', views.API_View_D, name='apiD'),
    path('api/v1/category/<int:cat_id>/', views.API_list, name='prod_list'),
    path('api/v1/category/', views.API_cat, name='cat')
    ]