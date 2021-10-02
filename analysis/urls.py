from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('ambulance/',views.ambulance, name='ambulance'),
    path('icubeds/',views.icubeds, name ='icubeds'),
    path('beds/',views.beds, name='beds'),
    path('oxygen/',views.oxygen, name='oxygen'),
    path('plasma/',views.plasma, name='plasma'),
    path('patient_status/',views.patient_status, name='patient_status'),
    path('search/',views.search, name='search'),
    path('graph/',views.graph, name='graph'),
    path('searchbed/',views.search_beds, name='search_beds'),
    path('searchicu/',views.search_icu, name='search_icu'),
    path('searchoxy/',views.search_oxygen, name='search_oxygen'),
    path('searchplasma/',views.search_plasma, name='search_plasma'),
    
]
