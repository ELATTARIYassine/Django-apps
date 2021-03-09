from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index"),
    path('<int:pk>/', views.FoodDetail.as_view(), name="detail"),
    path('add/', views.CreateItem.as_view(), name="create_item"),
    path('update/<int:pk_item>', views.update_item, name="update_item"),
    path('delete/<int:pk_item>', views.delete_item, name="delete_item"),
]