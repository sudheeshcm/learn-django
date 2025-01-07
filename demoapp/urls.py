from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('counter', views.counter, name='counter'),
    path('submit-counter', views.submit_counter, name='submit-counter')
]