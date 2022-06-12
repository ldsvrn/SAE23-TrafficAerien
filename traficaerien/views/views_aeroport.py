from django.shortcuts import render, redirect
from ..forms import AeroportForm
from .. import models
from ..models import Aeroport
from ..models import Vol
from django.http import HttpResponseRedirect
from django import forms

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