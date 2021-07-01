from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyFirstProject_index, name='MyFirstProject_index'),
    # path('<int:pk>/', views.MyFirstProject_detail, name="MyFirstProject_detail"),
    # path("<category>/", views.MyFirstProject_category, name='MyFirstProject_category'),
]