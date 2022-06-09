from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('ajout_avion/',views.ajout_avion),
    path("traitement_avion/",views.traitement_avion),
    path('ajout_piste/',views.ajout_piste),
    path("traitement_piste/",views.traitement_piste),
    path('ajout_vol/',views.ajout_vol),
    path("traitement_piste/",views.traitement_vol),
    path('ajout_aeroport/',views.ajout_aeroport),
    path('liste_aeroport/',views.liste_aeroport, name="list"),
    path('delete_aeroport/<int:id>/', views.delete_aeroport),

]
