from django.db import models

# Create your models here.
class aeroport(models.Model):
    nom = models.CharField(max_length = 100) 
    pays = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"Aéroport {self.nom} situé en {self.pays}."

class piste(models.Model):
    aeroport = models.ForeignKey(aeroport, on_delete=models.CASCADE)
    longeur = models.IntegerField()

    def __str__(self) -> str:
        return f"Piste situé dans l'aéroport {self.aeroport.nom} de {self.longeur}m."

class compagnie(models.Model):
    nom = models.CharField(max_length = 100) 
    description = models.CharField(max_length = 255)
    pays_de_rattachement = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f'Compagnie {self.nom}, "{self.description}", le pays de rattachement est {self.pays_de_rattachement}.'

class type_avion(models.Model):
    marque = models.CharField(max_length = 100) 
    modele = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    longueur_piste_necessaire = models.IntegerField()

    def __str__(self) -> str:
        return f"Avion {self.marque}, modèle {self.modele}, décrit comme {self.description}, \
        a besoin d'une piste de {self.longueur_piste_necessaire}m."

class avion(models.Model):
    nom = models.CharField(max_length = 100) 
    compagnie = models.ForeignKey(compagnie, on_delete=models.CASCADE)
    modele = models.ForeignKey(type_avion, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Avion {self.nom} de la compagnie {self.compagnie}, modèle {self.modele}."

class vol(models.Model):
    avion = models.ForeignKey(avion, on_delete=models.CASCADE)
    pilote = models.CharField(max_length = 100)
    aeroport_depart = models.ForeignKey(aeroport, on_delete=models.CASCADE)
    date_depart = models.DateField(blank=True, null = True)
    aeroport_arrive = models.ForeignKey(aeroport, on_delete=models.CASCADE)
    date_arrivee = models.DateField(blank=True, null = True)

    def __str__(self) -> str:
        return f"Vol: avion {self.avion.nom} piloté par {self.pilote}, \
            départ {self.aeroport_depart.nom} le {self.date_depart}, \
            arrivée {self.aeroport_arrive.nom} le {self.date_arrivee}."