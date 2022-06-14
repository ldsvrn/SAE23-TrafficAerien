from django.shortcuts import render, redirect
from ..forms import CompagnieForm
from .. import models
from ..models import Compagnie
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def ajout_compagnie(request):
    submitted = False
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/compagnie/liste")
    else:
        form = CompagnieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'compagnie/ajout_compagnie.html', {'form': form, 'submitted': submitted})


def liste_compagnie(request):
    compagnies = Compagnie.objects.all()
    return render(request, 'compagnie/liste_compagnie.html', {'compagnies': compagnies})


def delete_compagnie(request, id):
    compagnie_list = Compagnie.objects.get(idcompagnie=id)
    compagnie_list.delete()
    return HttpResponseRedirect("/compagnie/liste")


def modif_compagnie(request, id):
    obj = models.Compagnie.objects.get(idcompagnie=id)
    objform = CompagnieForm(model_to_dict(obj))
    if request.method == "POST":
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/compagnie/liste")
        else:
            return render(request, "compagnie/ajout_compagnie.html", {"form": form})
    else:
        return render(request, "compagnie/modif_compagnie.html", {"form": objform, "id": id})


def save_modif_compagnie(request, id):
    objform = CompagnieForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.idcompagnie = id
        objform.save()
        return HttpResponseRedirect("/compagnie/liste")
    else:
        return render(request, "compagnie/modif_compagnie.html", {"form": objform, "id": id})
