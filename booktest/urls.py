from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book_list'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('jojo', views.demo, name='demo'),
]
