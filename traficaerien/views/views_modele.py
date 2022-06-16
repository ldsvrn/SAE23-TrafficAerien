from django.shortcuts import render
from ..forms import ModeleForm
from .. import models
from ..models import Modele
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def ajout_modele(request):
    submitted = False
    if request.method == 'POST':
        form = ModeleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/modele/liste")
    else:
        form = ModeleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'modele/ajout_modele.html', {'form': form, 'submitted': submitted})


def liste_modele(request):
    modeles = Modele.objects.all()
    return render(request, 'modele/liste_modele.html', {'modeles': modeles})


def delete_modele(request, id):
    modele = Modele.objects.get(idmodele=id)
    modele.delete()
    return HttpResponseRedirect("/modele/liste")


def modif_modele(request, id):
    obj = models.Modele.objects.get(idmodele=id)
    objform = ModeleForm(model_to_dict(obj))
    if request.method == "POST":
        form = ModeleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/modele/liste")
        else:
            return render(request, "modele/ajout_modele.html", {"form": form})
    else:
        return render(request, "modele/modif_modele.html", {"form": objform, "id": id})


def save_modif_modele(request, id):
    objform = ModeleForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.idmodele = id
        objform.save()
        return HttpResponseRedirect("/modele/liste")
    else:
        return render(request, "modele/modif_modele.html", {"form": objform, "id": id})
