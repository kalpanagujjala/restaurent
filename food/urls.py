from django.urls import path
from food import views

urlpatterns=[
    path('info',views.home,name='myhome'),
    path('add',views.itemadd,name='add'),
]