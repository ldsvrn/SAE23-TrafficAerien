from django.shortcuts import render, redirect
from ..forms import AvionForm
from .. import models
from ..models import Avion
from ..models import Vol
from django.http import HttpResponseRedirect
from django import forms

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
    vols = Vol.objects.all()
    avions = Avion.objects.all()
    return render(request, 'avion/liste_avion.html', {'avions': avions, "vols": vols})


def delete_avion(request, id):
    avion_list = Avion.objects.get(id=id)
    avion_list.delete()
    return HttpResponseRedirect("/trafic/liste_avion/")