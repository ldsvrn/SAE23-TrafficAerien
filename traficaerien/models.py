# TODO: Fix les problèmes des OneToOne => config la BDD pour utiliser des FK, aeroports avec qu'un seule piste?
from django.db import models


class Aeroport(models.Model):
    idaeroport = models.AutoField(db_column='IdAeroport', primary_key=True)
    nomaeroport = models.CharField(db_column='NomAeroport', max_length=45)
    paysaeroport = models.CharField(db_column='PaysAeroport', max_length=45)

    def __str__(self) -> str:
        return f"{self.nomaeroport}, {self.paysaeroport}"

    class Meta:
        managed = False
        db_table = 'aeroport'


class Avion(models.Model):
    idavion = models.IntegerField(db_column='IdAvion', primary_key=True)
    idcompagnie = models.ForeignKey(
        'Compagnie', on_delete=models.CASCADE, db_column='IdCompagnie')
    idmodele = models.ForeignKey(
        'Modele', on_delete=models.CASCADE, db_column='IdModele')

    def __str__(self) -> str:
        return f"{self.idmodele.nommodele} de {self.idcompagnie.nomcompagnie}"

    class Meta:
        managed = False
        db_table = 'avion'


class Compagnie(models.Model):
    idcompagnie = models.IntegerField(
        db_column='IdCompagnie', primary_key=True)
    nomcompagnie = models.CharField(db_column='NomCompagnie', max_length=45)
    descricompagnie = models.TextField(db_column='DescriCompagnie')
    payscompagnie = models.CharField(db_column='PaysCompagnie', max_length=45)

    def __str__(self) -> str:
        return self.nomcompagnie

    class Meta:
        managed = False
        db_table = 'compagnie'


class Modele(models.Model):
    idmodele = models.AutoField(db_column='IdModele', primary_key=True)
    nommodele = models.CharField(db_column='NomModele', max_length=45)
    marquemodele = models.CharField(db_column='MarqueModele', max_length=45)
    typemodele = models.CharField(db_column='TypeModele', max_length=45)
    descrimodele = models.TextField(db_column='DescriModele')
    imagemodele = models.ImageField(db_column='ImageModele', upload_to="images/")
    longpistemodele = models.IntegerField(db_column='LongPisteModele')

    def __str__(self) -> str:
        return self.nommodele

    class Meta:
        managed = False
        db_table = 'modele'


class Piste(models.Model):
    idpiste = models.IntegerField(db_column='IdPiste', primary_key=True)
    longueurpiste = models.IntegerField(db_column='LongueurPiste')
    idaeroport = models.ForeignKey(
        Aeroport, on_delete=models.CASCADE, db_column='IdAeroport')

    class Meta:
        managed = False
        db_table = 'piste'


class Vol(models.Model):
    idvol = models.IntegerField(db_column='IdVol', primary_key=True)
    idavion = models.ForeignKey(
        Avion, on_delete=models.CASCADE, db_column='IdAvion')
    pilotevol = models.CharField(db_column='PiloteVol', max_length=45)
    idaeroportdepart = models.ForeignKey(
        Aeroport, on_delete=models.CASCADE, db_column='IdAeroportDepart', related_name="depart")
    idaeroportarrivee = models.ForeignKey(
        Aeroport, on_delete=models.CASCADE, db_column='IdAeroportArrivee', related_name="arrivee")
    datedepartvol = models.DateTimeField(db_column='DateDepartVol')
    datearriveevol = models.DateTimeField(db_column='DateArriveeVol')

    def __str__(self) -> str:
        return f"Vol du {self.datedepartvol} de {self.idaeroportdepart.nomaeroport} vers {self.idaeroportarrivee.nomaeroport}"

    class Meta:
        managed = False
        db_table = 'vol'
