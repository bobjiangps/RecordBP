from django.urls import path
from . import views

urlpatterns = [
    path('<str:filename>/', views.show_file_content, name='show_file_content'),
]
