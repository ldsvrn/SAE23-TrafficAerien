from django.shortcuts import render, redirect
from ..forms import CompagnieForm
from .. import models
from ..models import Compagnie
from django.http import HttpResponseRedirect
from django import forms

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