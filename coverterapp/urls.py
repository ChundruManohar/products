from django.urls import path

from .import views 

urlpatterns = [
    path('showpro/',views.show_p,name='show'),
    path('create-pdf/',views.pdfreo,name='create-pdf'),
]
