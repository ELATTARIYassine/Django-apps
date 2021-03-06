from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk_item>/', views.detail, name="detail"),
    path('add/', views.create_item, name="create_item"),
    path('update/<int:pk_item>', views.update_item, name="update_item"),
    path('delete/<int:pk_item>', views.delete_item, name="delete_item"),
]