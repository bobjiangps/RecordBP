from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list_page, name='person_list'),
    path('find_person', views.find_person_list_page, name='find_person_list'),
    path('login/', views.do_login, name='do_login'),
    path('logout/', views.do_logout, name='do_logout'),
]
