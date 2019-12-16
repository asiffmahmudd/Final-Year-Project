from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.hotel_index, name='hotel_index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.getLogin, name ='login'),
    path('logout', views.getLogout, name ='logout'),
    path('search', views.searchProduct, name ='search'),
    path('tablesorter', views.tablesorter, name ='tablesorter'),
    path('searchtable', views.searchTable, name ='searchTable'),



    #path('details/<product_url>', views.getDetails, name ='details'),



]