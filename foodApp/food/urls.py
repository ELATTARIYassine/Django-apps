from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk_item>/', views.detail, name="detail")
]