from django.shortcuts import render, redirect
from .forms import AeroportForm
from .forms import PisteForm
from .forms import CompagnieForm
from .forms import AvionTypeForm
from .forms import AvionForm
from .forms import VolForm
from . import models
from .models import aeroport
from .models import piste
from .models import compagnie
from .models import type_avion
from .models import avion
from .models import vol
from django.http import HttpResponseRedirect
from django import forms

def main(request):
    liste = avion.objects.all()
    liste1 = piste.objects.all()
    liste2 = vol.objects.all()
    return render(request, 'main.html', {'liste': liste})
    return render(request, 'main.html', {'liste1': liste1})
    return render(request, 'main.html', {'liste2': liste2})

def ajout_avion(request):
    if request.method == "POST":
        form = AvionForm(request)
        if form.is_valid():
            joueur = form.save()
            return HttpResponseRedirect("/traficaerien/")
        else:
            return render(request,"ajout_avion.html",{"form": form})
    else :
        form = AvionForm()
        return render(request,"ajout_avion.html",{"form" : form})



def traitement_avion(request):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save(commit=False)
        avion.save()
        return HttpResponseRedirect("/traficaerien/")
    else:
        return render(request,"ajout_avion.html",{"form": lform})

def ajout_piste(request):
    if request.method == "POST":
        form = PisteForm(request)
        if form.is_valid():
            piste = form.save()
            return HttpResponseRedirect("/traficaerien/")
        else:
            return render(request,"ajout_piste.html",{"form": form})
    else :
        form = PisteForm()
        return render(request,"ajout_piste.html",{"form" : form})

def traitement_piste(request):
    lform = PisteForm(request.POST)
    if lform.is_valid():
        piste = lform.save(commit=False)
        piste.save()
        return HttpResponseRedirect("/traficaerien/")
    else:
        return render(request,"ajout_piste.html",{"form": lform})

def ajout_vol(request):
    if request.method == "POST":
        form = VolForm(request)
        if form.is_valid():
            vol = form.save()
            return HttpResponseRedirect("/traficaerien/")
        else:
            return render(request,"ajout_vol.html",{"form": form})
    else :
        form = VolForm()
        return render(request,"ajout_vol.html",{"form" : form})

def traitement_vol(request):
    lform = VolForm(request.POST)
    if lform.is_valid():
        vol = lform.save(commit=False)
        vol.save()
        return HttpResponseRedirect("/traficaerien/")
    else:
        return render(request,"ajout_vol.html",{"form": lform})

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
    return render(request, 'ajout_aeroport.html', {'form':form, 'submitted':submitted})

def liste_aeroport(request):
   liste = vol.objects.all()
   liste_aeroport = aeroport.objects.all()
   return render(request, 'liste_aeroport.html', {'liste_aeroport': liste_aeroport,"liste":liste})

def update_aeroport(request, id):
    aeroport_list = aeroport.objects.get(pk=id)
    form = AeroportForm(request.POST or None, instance=aeroport_list)
    if form.is_valid():
        form.save()
        return redirect("aeroport")
    return render(request, 'update_aeroport.html', {'aeroport':aeroport, 'form':form})

def delete_aeroport(request, id):
    aeroport_list = aeroport.objects.get(id=id)
    aeroport_list.delete()
    return HttpResponseRedirect("/trafic/liste_aeroport/")

