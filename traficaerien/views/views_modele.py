from django.shortcuts import render, redirect
from ..forms import ModeleForm
from .. import models
from ..models import Modele
from django.http import HttpResponseRedirect
from django import forms

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