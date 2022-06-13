from django.shortcuts import render, redirect
from ..forms import ModeleForm
from .. import models
from ..models import Modele
from django.http import HttpResponseRedirect
from django import forms

def ajout_modele(request):
    submitted = False
    if request.method == 'POST':
        form =ModeleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/modele/liste")
    else:
        form = ModeleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'modele/ajout_modele.html', {'form':form, 'submitted':submitted})

def liste_modele(request):
   modeles = Modele.objects.all()
   return render(request, 'modele/liste_modele.html', {'modeles': modeles})


def delete_modele(request, id):
    modele = Modele.objects.get(id=id)
    modele.delete()
    return HttpResponseRedirect("/modele/liste")