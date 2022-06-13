from django.shortcuts import render, redirect
from ..forms import AeroportForm
from ..forms import PisteForm
from ..forms import CompagnieForm
from ..forms import ModeleForm
from ..forms import AvionForm
from ..forms import VolForm
from .. import models
from ..models import Aeroport
from ..models import Piste
from ..models import Compagnie
from ..models import Modele
from ..models import Avion
from ..models import Vol
from django.http import HttpResponseRedirect
from django import forms

def main(request):
    liste = Avion.objects.all()
    return render(request, 'main.html', {'liste': liste})
    