from django.urls import path

from . import views

urlpatterns = [
    path('submit',views.submit, name='add'),
    path('',views.index, name = 'home')
]