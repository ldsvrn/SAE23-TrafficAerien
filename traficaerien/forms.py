from dataclasses import field
from django import forms
from django.forms import ModelForm, Form, MultipleChoiceField, CharField, DateField, NumberInput
from . import models

class AeroportForm(ModelForm):
    class Meta:
        model = models.Aeroport
        fields = ('nomaeroport', 'paysaeroport')
        #fields = ('nom', 'pays')
        labels = {
            'nomaeroport' : 'Nom',
            'paysaeroport' : 'Pays'
        }

class PisteForm(ModelForm):
    class Meta:
        model = models.Piste
        fields = ('longueurpiste', 'idaeroport')
        labels = {
            'longueurpiste' : 'Longueur de la piste' ,
            'idaeroport': 'Aéroport'
        }

class CompagnieForm(ModelForm):
    class Meta:
        model = models.Compagnie
        fields = ('nomcompagnie', 'descricompagnie', 'payscompagnie')
        labels = {
            'nomcompagnie' : 'Nom',
            'descricompagnie' : 'Description' ,
            'payscompagnie' : 'Pays de rattachement'
        }

class ModeleForm(ModelForm):
    class Meta:
        model = models.Modele
        fields = ('nommodele', 'marquemodele', 'typemodele', 'descrimodele', 'imagemodele', 'longpistemodele')
        labels = {
            'nommodele' : 'Nom',
            'marquemodele' : 'Marque' ,
            'typemodele' : 'Type de modèle',
            'descrimodele': 'Description',
            'imagemodele': 'Image',
            'longpistemodele': 'Longueur piste nécessaire'
        }

class AvionForm(ModelForm):
    class Meta:
        model = models.Avion
        fields = ('idcompagnie', 'idmodele')
        labels = {
            'idcompagnie' : 'Compagnie',
            'idmodele' : 'Modèle' 
        }

class VolForm(ModelForm):
    class Meta:
        model = models.Vol
        fields = ('idavion', 'pilotevol', 'idaeroportdepart', 'idaeroportarrivee', 'datedepartvol', 'datearriveevol')
        labels = {
            'idavion' : 'Avion',
            'pilotevol' : 'Pilote' ,
            'idaeroportdepart' : 'Aéroport de départ',
            'idaeroportarrivee': "Aéroport d'arrivée",
            'datedepartvol': 'Date de départ',
            'datearriveevol': "Date d'arrivée"
        }