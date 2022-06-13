from django.shortcuts import render, redirect
from ..forms import PisteForm
from ..models import Piste
from django.http import HttpResponseRedirect
from django import forms


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
   pistes= Piste.objects.all()
   return render(request, 'piste/liste_piste.html', {'pistes': pistes})


def delete_piste(request, id):
    piste_list = Piste.objects.get(id=id)
    piste_list.delete()
    return HttpResponseRedirect("/trafic/liste_piste/")