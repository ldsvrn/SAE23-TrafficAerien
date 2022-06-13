from django.shortcuts import render, redirect
from ..forms import VolForm
from .. import models
from ..models import Vol
from django.http import HttpResponseRedirect
from django import forms

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
   vols = Vol.objects.all()
   return render(request, 'vol/liste_vol.html', {'vols': vols})

def delete_vol(request, id):
    vol_list = Vol.objects.get(id=id)
    vol_list.delete()
    return HttpResponseRedirect("/trafic/liste_vol/")