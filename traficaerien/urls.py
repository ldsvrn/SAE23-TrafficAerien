from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('avion/ajout',views.ajout_avion),
    path("avion/liste",views.liste_avion),
    path('avion/suppr/<int:id>', views.delete_avion),

    path('piste/ajout',views.ajout_piste),
    path("piste/liste",views.liste_piste),
    path('piste/suppr/<int:id>', views.delete_piste),

    path('vol/ajout',views.ajout_vol),
    path("vol/liste",views.liste_vol),
    path('vol/suppr/<int:id>', views.delete_vol),

    path('aeroport/ajout',views.ajout_aeroport),
    path('aeroport/liste',views.liste_aeroport),
    path('aeroport/suppr/<int:id>', views.delete_aeroport),

    path('compagnie/ajout',views.ajout_compagnie),
    path('compagnie/liste',views.liste_compagnie),
    path('compagnie/suppr/<int:id>/', views.delete_compagnie),

    path('modele/ajout',views.ajout_aviontype),
    path('modele/liste',views.liste_aviontype),
    path('modele/suppr/<int:id>/', views.delete_aviontype),
]
