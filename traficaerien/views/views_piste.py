from django.shortcuts import render, redirect
from ..forms import PisteForm
from .. import models
from ..models import Piste
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def ajout_piste(request):
    submitted = False
    if request.method == 'POST':
        form = PisteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/piste/liste")
    else:
        form = PisteForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'piste/ajout_piste.html', {'form': form, 'submitted': submitted})


def liste_piste(request):
    pistes = Piste.objects.all()
    return render(request, 'piste/liste_piste.html', {'pistes': pistes})


def delete_piste(request, id):
    piste_list = Piste.objects.get(idpiste=id)
    piste_list.delete()
    return HttpResponseRedirect("/piste/liste")


def modif_piste(request, id):
    obj = models.Piste.objects.get(idpiste=id)
    objform = PisteForm(model_to_dict(obj))
    if request.method == "POST":
        form = PisteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/piste/liste")
        else:
            return render(request, "piste/ajout_piste.html", {"form": form})
    else:
        return render(request, "piste/modif_piste.html", {"form": objform, "id": id})


def save_modif_piste(request, id):
    objform = PisteForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.idpiste = id
        objform.save()
        return HttpResponseRedirect("/piste/liste")
    else:
        return render(request, "piste/modif_piste.html", {"form": objform, "id": id})
