#TODO: Fix les problèmes des OneToOne => config la BDD pour utiliser des FK, aeroports avec qu'un seule piste?
from django.db import models

class Aeroport(models.Model):
    idaeroport = models.AutoField(db_column='IdAeroport', primary_key=True)  # Field name made lowercase.
    nomaeroport = models.CharField(db_column='NomAeroport', max_length=45)  # Field name made lowercase.
    paysaeroport = models.CharField(db_column='PaysAeroport', max_length=45)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nomaeroport

    class Meta:
        managed = False
        db_table = 'aeroport'


class Avion(models.Model):
    idavion = models.IntegerField(db_column='IdAvion', primary_key=True)  # Field name made lowercase.
    idcompagnie = models.OneToOneField('Compagnie', on_delete=models.CASCADE, db_column='IdCompagnie')  # Field name made lowercase.
    idmodele = models.OneToOneField('Modele', on_delete=models.CASCADE, db_column='IdModele')  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.idmodele.nommodele} de {self.idcompagnie.nomcompagnie}"

    class Meta:
        managed = False
        db_table = 'avion'


class Compagnie(models.Model):
    idcompagnie = models.IntegerField(db_column='IdCompagnie', primary_key=True)  # Field name made lowercase.
    nomcompagnie = models.CharField(db_column='NomCompagnie', max_length=45)  # Field name made lowercase.
    descricompagnie = models.TextField(db_column='DescriCompagnie')  # Field name made lowercase.
    payscompagnie = models.CharField(db_column='PaysCompagnie', max_length=45)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nomcompagnie

    class Meta:
        managed = False
        db_table = 'compagnie'


class Modele(models.Model):
    idmodele = models.AutoField(db_column='IdModele', primary_key=True)  # Field name made lowercase.
    nommodele = models.CharField(db_column='NomModele', max_length=45)  # Field name made lowercase.
    marquemodele = models.CharField(db_column='MarqueModele', max_length=45)  # Field name made lowercase.
    typemodele = models.CharField(db_column='TypeModele', max_length=45)  # Field name made lowercase.
    descrimodele = models.TextField(db_column='DescriModele')  # Field name made lowercase.
    imagemodele = models.TextField(db_column='ImageModele')  # Field name made lowercase.
    longpistemodele = models.IntegerField(db_column='LongPisteModele')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nommodele

    
    class Meta:
        managed = False
        db_table = 'modele'


class Piste(models.Model):
    idpiste = models.IntegerField(db_column='IdPiste', primary_key=True)  # Field name made lowercase.
    longueurpiste = models.IntegerField(db_column='LongueurPiste')  # Field name made lowercase.
    idaeroport = models.OneToOneField(Aeroport, on_delete=models.CASCADE, db_column='IdAeroport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'piste'


class Vol(models.Model):
    idvol = models.IntegerField(db_column='IdVol', primary_key=True)  # Field name made lowercase.
    idavion = models.OneToOneField(Avion, on_delete=models.CASCADE, db_column='IdAvion')  # Field name made lowercase.
    pilotevol = models.CharField(db_column='PiloteVol', max_length=45)  # Field name made lowercase.
    idaeroportdepart = models.OneToOneField(Aeroport, on_delete=models.CASCADE, db_column='IdAeroportDepart', related_name="depart")  # Field name made lowercase.
    idaeroportarrivee = models.OneToOneField(Aeroport, on_delete=models.CASCADE, db_column='IdAeroportArrivee', related_name="arrivee")  # Field name made lowercase.
    datedepartvol = models.DateTimeField(db_column='DateDepartVol')  # Field name made lowercase.
    datearriveevol = models.DateTimeField(db_column='DateArriveeVol')  # Field name made lowercase.

    def __str__(self) -> str:
        return f"Vol du {self.datedepartvol} de {self.idaeroportdepart.nomaeroport} vers {self.idaeroportarrivee.nomaeroport}"

    class Meta:
        managed = False
        db_table = 'vol'
