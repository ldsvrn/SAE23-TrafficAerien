from django.shortcuts import render, redirect
from .forms import AeroportForm
from .forms import PisteForm
from .forms import CompagnieForm
from .forms import ModeleForm
from .forms import AvionForm
from .forms import VolForm
from . import models
from .models import Aeroport
from .models import Piste
from .models import Compagnie
from .models import Modele
from .models import Avion
from .models import Vol
from django.http import HttpResponseRedirect
from django import forms

def main(request):
    liste = Avion.objects.all()
    return render(request, 'main.html', {'liste': liste})


def ajout_avion(request):
    submitted = False
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_avion/")
    else:
        form = AvionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'avion/ajout_avion.html', {'form':form, 'submitted':submitted})


def liste_avion(request):
    liste = Vol.objects.all()
    liste_avion = Avion.objects.all()
    return render(request, 'avion/liste_avion.html', {'liste_avion': liste_avion,"liste":liste})


def delete_avion(request, id):
    avion_list = Avion.objects.get(id=id)
    avion_list.delete()
    return HttpResponseRedirect("/trafic/liste_avion/")

def ajout_piste(request):
    submitted = False
    if request.method == 'POST':
        form =PisteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_piste/")
    else:
        form = PisteForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'piste/ajout_piste.html', {'form':form, 'submitted':submitted})

def liste_piste(request):
   liste = Piste.objects.all()
   liste_piste= Piste.objects.all()
   return render(request, 'piste/liste_piste.html', {'liste_piste': liste_piste,"liste":liste})


def delete_piste(request, id):
    piste_list = Piste.objects.get(id=id)
    piste_list.delete()
    return HttpResponseRedirect("/trafic/liste_piste/")



def ajout_vol(request):
    submitted = False
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_vol/")
    else:
        form = VolForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'vol/ajout_vol.html', {'form':form, 'submitted':submitted})

def liste_vol(request):
   liste = Vol.objects.all()
   liste_vol= Vol.objects.all()
   return render(request, 'vol/liste_vol.html', {'liste_vol': liste_vol,"liste":liste})

def delete_vol(request, id):
    vol_list = Vol.objects.get(id=id)
    vol_list.delete()
    return HttpResponseRedirect("/trafic/liste_vol/")

def ajout_aeroport(request):
    submitted = False
    if request.method == 'POST':
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_aeroport/")
    else:
        form = AeroportForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'aeroport/ajout_aeroport.html', {'form':form, 'submitted':submitted})

def liste_aeroport(request):
   liste = Vol.objects.all()
   liste_aeroport = Aeroport.objects.all()
   return render(request, 'aeroport/liste_aeroport.html', {'liste_aeroport': liste_aeroport,"liste":liste})

def delete_aeroport(request, id):
    aeroport_list = Aeroport.objects.get(id=id)
    aeroport_list.delete()
    return HttpResponseRedirect("/trafic/liste_aeroport/")

def ajout_compagnie(request):
    submitted = False
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_compagnie/")
    else:
        form = CompagnieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'compagnie/ajout_compagnie.html', {'form':form, 'submitted':submitted})

def liste_compagnie(request):
   liste = Compagnie.objects.all()
   liste_compagnie= Compagnie.objects.all()
   return render(request, 'compagnie/liste_compagnie.html', {'liste_compagnie': liste_compagnie,"liste":liste})

def delete_compagnie(request, id):
    compagnie_list = Compagnie.objects.get(id=id)
    compagnie_list.delete()
    return HttpResponseRedirect("/trafic/liste_compagnie/")


def ajout_aviontype(request):
    submitted = False
    if request.method == 'POST':
        form =ModeleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/trafic/liste_aviontype/")
    else:
        form = ModeleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'modele/ajout_aviontype.html', {'form':form, 'submitted':submitted})

def liste_aviontype(request):
   liste = Modele.objects.all()
   liste_aviontype= Modele.objects.all()
   return render(request, 'modele/liste_aviontype.html', {'liste_aviontype': liste_aviontype,"liste":liste})


def delete_aviontype(request, id):
    aviontype_list = Modele.objects.get(id=id)
    aviontype_list.delete()
    return HttpResponseRedirect("/trafic/liste_aviontype/")

