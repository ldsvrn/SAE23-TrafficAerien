from dataclasses import field
from django import forms
from django.forms import ModelForm, Form, MultipleChoiceField, CharField, DateField, NumberInput
from . import models

class AeroportForm(ModelForm):
    class Meta:
        model = models.aeroport
        fields = "__all__"
        #fields = ('nom', 'pays')
        labels = {
            'nom' : 'Nom',
            'pays' : 'Pays'
        }

class PisteForm(ModelForm):
    class Meta:
        model = models.piste
        fields = "__all__"
        labels = {
            'nom' : 'Nom',
            'longueur' : 'Longueur de la piste' 
        }

class CompagnieForm(ModelForm):
    class Meta:
        model = models.compagnie
        fields = "__all__"
        labels = {
            'nom' : 'Nom',
            'description' : 'Description' ,
            'pays_de_rattachement' : 'Pays de rattachement'
        }

class AvionTypeForm(ModelForm):
    class Meta:
        model = models.type_avion
        fields = "__all__"
        labels = {
            'marque' : 'Marque',
            'modele' : 'Modèle' ,
            'description' : 'Description',
            'image': 'Image',
            'longueur_piste_necessaire': 'Longueur piste nécessaire'
        }

class AvionForm(ModelForm):
    class Meta:
        model = models.avion
        fields = "__all__"
        labels = {
            'nom' : 'Nom',
            'compagnie' : 'Compagnie' ,
            'modele' : 'Modèle'
        }

class VolForm(ModelForm):
    class Meta:
        model = models.vol
        fields = "__all__"
        labels = {
            'avion' : 'Avion',
            'pilote' : 'Pilote' ,
            'aeroport_depart' : 'Aéroport de départ',
            'date_depart': 'Date de départ',
            'aeroport_arrivee': "Aéroport d'arrivée",
            'date_arrivee': "Date d'arrivée"
        }