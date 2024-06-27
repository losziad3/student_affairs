from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('add',views.add, name='add'),    
    path('edit/<int:id>',views.edit, name='edit'),
    path('update',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),       
    path('about', views.about, name='about'),
    path('list', views.list_student, name='list'),
    path('search',views.Search, name='search'),
    path('searchajax',views.Searchajax, name='search_ajax'),

]