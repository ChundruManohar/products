from django.urls import path
from .import views
urlpatterns = [
    path('',views.Showproducts,name='showproduct'),
    path('details/<int:pk>/',views.productdetails,name='productdetails'),
    path('add/',views.addproduct,name='addproduct'),
    path('search/',views.searchbar,name='searchbar'),
    path('update/<int:pk>/',views.updateproduct,name='updateproduct'),   
    path('delete/<int:pk>/',views.deleteproduct,name="deleteproduct"),
    path('details/<int:pk>/add-comment/',views.add_comment,name="add-comment"),
    
    
]