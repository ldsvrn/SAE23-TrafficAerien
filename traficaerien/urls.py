from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('avion/ajout',views.ajout_avion),
    path("avion/liste",views.liste_avion),
    path('avion/suppr/<int:id>', views.delete_avion),
    path('avion/modif/<int:id>', views.modif_avion),
    path('avion/save/<int:id>', views.save_modif_avion),

    path('piste/ajout',views.ajout_piste),
    path("piste/liste",views.liste_piste),
    path('piste/suppr/<int:id>', views.delete_piste),
    path('piste/modif/<int:id>', views.modif_piste),
    path('piste/save/<int:id>', views.save_modif_piste),

    path('vol/ajout',views.ajout_vol),
    path("vol/liste",views.liste_vol),
    path('vol/suppr/<int:id>', views.delete_vol),
    path('vol/modif/<int:id>', views.modif_vol),
    path('vol/save/<int:id>', views.save_modif_vol),

    path('aeroport/ajout',views.ajout_aeroport),
    path('aeroport/liste',views.liste_aeroport),
    path('aeroport/suppr/<int:id>', views.delete_aeroport),
    path('aeroport/modif/<int:id>', views.modif_aeroport),
    path('aeroport/save/<int:id>', views.save_modif_aeroport),
    path('aeroport/pistes/<int:id>', views.liste_aeroport_piste),
    path('aeroport/vols_arrivee/<int:id>', views.liste_aeroports_vols_arrivee),
    path('aeroport/vols_depart/<int:id>', views.liste_aeroports_vols_depart),

    path('compagnie/ajout',views.ajout_compagnie),
    path('compagnie/liste',views.liste_compagnie),
    path('compagnie/suppr/<int:id>/', views.delete_compagnie),
    path('compagnie/modif/<int:id>', views.modif_compagnie),
    path('compagnie/save/<int:id>', views.save_modif_compagnie),

    path('modele/ajout',views.ajout_modele),
    path('modele/liste',views.liste_modele),
    path('modele/suppr/<int:id>/', views.delete_modele),
    path('modele/modif/<int:id>', views.modif_modele),
    path('modele/save/<int:id>', views.save_modif_modele),
]
