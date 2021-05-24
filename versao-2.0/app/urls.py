from django.urls import path
from . import views


urlpatterns = [
    path('', views.livro_list, name='livro_list'),
    path('livro/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livro/new/', views.livro_new, name='livro_new'),
]