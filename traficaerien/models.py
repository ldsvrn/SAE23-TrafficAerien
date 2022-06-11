# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import CASCADE
from django.db import models


class Aeroport(models.Model):
    idaeroport = models.AutoField(db_column='IdAeroport', primary_key=True)  # Field name made lowercase.
    nomaeroport = models.CharField(db_column='NomAeroport', max_length=45)  # Field name made lowercase.
    paysaeroport = models.CharField(db_column='PaysAeroport', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aeroport'


class Avion(models.Model):
    idavion = models.IntegerField(db_column='IdAvion', primary_key=True)  # Field name made lowercase.
    idcompagnie = models.OneToOneField('Compagnie', on_delete=CASCADE, db_column='IdCompagnie')  # Field name made lowercase.
    idmodele = models.OneToOneField('Modele', on_delete=CASCADE, db_column='IdModele')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'avion'


class Compagnie(models.Model):
    idcompagnie = models.IntegerField(db_column='IdCompagnie', primary_key=True)  # Field name made lowercase.
    nomcompagnie = models.CharField(db_column='NomCompagnie', max_length=45)  # Field name made lowercase.
    descricompagnie = models.TextField(db_column='DescriCompagnie')  # Field name made lowercase.
    payscompagnie = models.CharField(db_column='PaysCompagnie', max_length=45)  # Field name made lowercase.

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

    class Meta:
        managed = False
        db_table = 'modele'


class Piste(models.Model):
    idpiste = models.IntegerField(db_column='IdPiste', primary_key=True)  # Field name made lowercase.
    longueurpiste = models.IntegerField(db_column='LongueurPiste')  # Field name made lowercase.
    idaeroport = models.OneToOneField(Aeroport, on_delete=CASCADE, db_column='IdAeroport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'piste'


class Vol(models.Model):
    idvol = models.IntegerField(db_column='IdVol', primary_key=True)  # Field name made lowercase.
    idavion = models.OneToOneField(Avion, on_delete=CASCADE, db_column='IdAvion')  # Field name made lowercase.
    pilotevol = models.CharField(db_column='PiloteVol', max_length=45)  # Field name made lowercase.
    idaeroportdepart = models.OneToOneField(Aeroport, on_delete=CASCADE, db_column='IdAeroportDepart', related_name="depart")  # Field name made lowercase.
    idaeroportarrivee = models.OneToOneField(Aeroport, on_delete=CASCADE, db_column='IdAeroportArrivee', related_name="arrivee")  # Field name made lowercase.
    datedepartvol = models.DateTimeField(db_column='DateDepartVol')  # Field name made lowercase.
    datearriveevol = models.DateTimeField(db_column='DateArriveeVol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vol'
