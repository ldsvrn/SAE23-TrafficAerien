from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('ajout_avion/',views.ajout_avion),
    path("liste_avion/",views.liste_avion),
    path('delete_avion/<int:id>/', views.delete_avion),
    path('ajout_piste/',views.ajout_piste),
    path("liste_piste/",views.liste_piste),
    path('delete_piste/<int:id>/', views.delete_piste),
    path('ajout_vol/',views.ajout_vol),
    path("liste_vol/",views.liste_vol),
    path('delete_vol/<int:id>/', views.delete_vol),
    path('ajout_aeroport/',views.ajout_aeroport),
    path('liste_aeroport/',views.liste_aeroport),
    path('delete_aeroport/<int:id>/', views.delete_aeroport),
    path('ajout_compagnie/',views.ajout_compagnie),
    path('liste_compagnie/',views.liste_compagnie),
    path('delete_compagnie/<int:id>/', views.delete_compagnie),
    path('ajout_aviontype/',views.ajout_aviontype),
    path('liste_aviontype/',views.liste_aviontype),
    path('delete_aviontype/<int:id>/', views.delete_aviontype),

]
