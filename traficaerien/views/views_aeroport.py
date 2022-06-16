from django.shortcuts import render, redirect
from ..forms import AeroportForm
from .. import models
from ..models import Aeroport
from ..models import Vol
from django.http import HttpResponseRedirect, FileResponse
from django.forms.models import model_to_dict
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.lib.units import cm
import io


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
    aeroports = Aeroport.objects.all()
    return render(request, 'aeroport/liste_aeroport.html', {'aeroports': aeroports})


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


def liste_aeroport_piste(request, id):
    piste = models.Piste.objects.filter(idaeroport = id)
    return render(request, 'piste/liste_piste.html', {'pistes': piste})


def liste_aeroports_vols_arrivee(request, id):
    vols = models.Vol.objects.filter(idaeroportarrivee = id)
    return render(request, 'vol/liste_vol.html', {'vols': vols})


def liste_aeroports_vols_depart(request, id):
    vols = models.Vol.objects.filter(idaeroportdepart = id)
    return render(request, 'vol/liste_vol.html', {'vols': vols})


def fiche_de_vols(request, id):
    aeroport = models.Aeroport.objects.get(idaeroport=id)
    vols = models.Vol.objects.filter(idaeroportdepart = id)
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer, pagesize=A4)
    p.drawString(cm, 28*cm, f"Vols partant de l'aéroport {aeroport}")
    data = [["Avion", "Pilote", "Vers", "Départ", "Arrivée"]]
    for vol in vols:
        data.append([
            vol.idavion.idmodele.nommodele, 
            vol.pilotevol,
            vol.idaeroportarrivee.nomaeroport,
            vol.datedepartvol,
            vol.datearriveevol
            ])
    print(data)
    t=Table(data)
    t.wrapOn(p, 25*cm,100)
    t.drawOn(p, cm, 25*cm)
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"fiche-vol-{aeroport.nomaeroport}.pdf")