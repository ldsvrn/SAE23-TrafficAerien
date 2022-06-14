from django.shortcuts import render, redirect
from ..forms import AvionForm
from .. import models
from ..models import Avion
from ..models import Vol
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

def ajout_avion(request):
    submitted = False
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/avion/liste")
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
    avion_list = Avion.objects.get(idavion=id)
    avion_list.delete()
    return HttpResponseRedirect("/avion/liste")


def modif_avion(request, id):
    obj = models.Avion.objects.get(idavion=id)
    objform = AvionForm(model_to_dict(obj))
    if request.method == "POST": 
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/avion/liste")
        else:
            return render(request,"avion/ajout_avion.html",{"form": form})
    else :
        return render(request, "avion/modif_avion.html", {"form": objform, "id": id})


def save_modif_avion(request, id):
    objform = AvionForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.idavion = id;
        objform.save()
        return HttpResponseRedirect("/avion/liste")
    else:
        return render(request, "avion/modif_avion.html", {"form": objform, "id": id})