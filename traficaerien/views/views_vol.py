from django.shortcuts import render, redirect
from ..forms import VolForm
from .. import models
from ..models import Vol
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


def ajout_vol(request):
    submitted = False
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/vol/liste")
    else:
        form = VolForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'vol/ajout_vol.html', {'form': form, 'submitted': submitted})


def liste_vol(request):
    vols = Vol.objects.all()
    return render(request, 'vol/liste_vol.html', {'vols': vols})


def delete_vol(request, id):
    vol_list = Vol.objects.get(idvol=id)
    vol_list.delete()
    return HttpResponseRedirect("/vol/liste")


def modif_vol(request, id):
    obj = models.Vol.objects.get(idvol=id)
    objform = VolForm(model_to_dict(obj))
    if request.method == "POST":
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/vol/liste")
        else:
            return render(request, "vol/ajout_vol.html", {"form": form})
    else:
        return render(request, "vol/modif_vol.html", {"form": objform, "id": id})


def save_modif_vol(request, id):
    objform = VolForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.idvol = id
        objform.save()
        return HttpResponseRedirect("/vol/liste")
    else:
        return render(request, "vol/modif_vol.html", {"form": objform, "id": id})
