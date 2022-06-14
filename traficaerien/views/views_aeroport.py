from django.shortcuts import render, redirect
from ..forms import AeroportForm
from .. import models
from ..models import Aeroport
from ..models import Vol
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def ajout_aeroport(request):
    submitted = False
    if request.method == 'POST':
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/aeroport/liste")
    else:
        form = AeroportForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'aeroport/ajout_aeroport.html', {'form': form, 'submitted': submitted})


def liste_aeroport(request):
    vols = Vol.objects.all()
    aeroports = Aeroport.objects.all()
    return render(request, 'aeroport/liste_aeroport.html', {'aeroports': aeroports, "vols": vols})


def delete_aeroport(request, id):
    aeroport_list = Aeroport.objects.get(idaeroport=id)
    aeroport_list.delete()
    return HttpResponseRedirect("/aeroport/liste")


def modif_aeroport(request, id):
    aeroport = models.Aeroport.objects.get(idaeroport=id)
    aeroform = AeroportForm(model_to_dict(aeroport))
    if request.method == "POST":
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/aeroport/liste")
        else:
            return render(request, "aeroport/ajout_aeroport.html", {"form": form})
    else:
        return render(request, "aeroport/modif_aeroport.html", {"form": aeroform, "id": id})


def save_modif_aeroport(request, id):
    aeroform = AeroportForm(request.POST)
    if aeroform.is_valid():
        aeroform = aeroform.save(commit=False)
        aeroform.idaeroport = id
        aeroform.save()
        return HttpResponseRedirect("/aeroport/liste")
    else:
        return render(request, "aeroport/modif_aeroport.html", {"form": aeroform, "id": id})
