# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aeroport(models.Model):
    idaeroport = models.AutoField(db_column='IdAeroport', primary_key=True)  # Field name made lowercase.
    nomaeroport = models.CharField(db_column='NomAeroport', max_length=45)  # Field name made lowercase.
    paysaeroport = models.CharField(db_column='PaysAeroport', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aeroport'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Avion(models.Model):
    idavion = models.IntegerField(db_column='IdAvion', primary_key=True)  # Field name made lowercase.
    idcompagnie = models.ForeignKey('Compagnie', models.DO_NOTHING, db_column='IdCompagnie')  # Field name made lowercase.
    idmodele = models.ForeignKey('Modele', models.DO_NOTHING, db_column='IdModele')  # Field name made lowercase.

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    idaeroport = models.ForeignKey(Aeroport, models.DO_NOTHING, db_column='IdAeroport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'piste'


class TraficaerienAeroport(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'traficaerien_aeroport'


class TraficaerienAvion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    compagnie = models.ForeignKey('TraficaerienCompagnie', models.DO_NOTHING)
    modele = models.ForeignKey('TraficaerienTypeAvion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'traficaerien_avion'


class TraficaerienCompagnie(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    pays_de_rattachement = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'traficaerien_compagnie'


class TraficaerienPiste(models.Model):
    id = models.BigAutoField(primary_key=True)
    longeur = models.IntegerField()
    aeroport = models.ForeignKey(TraficaerienAeroport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'traficaerien_piste'


class TraficaerienTypeAvion(models.Model):
    id = models.BigAutoField(primary_key=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=100, blank=True, null=True)
    longueur_piste_necessaire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'traficaerien_type_avion'


class TraficaerienVol(models.Model):
    id = models.BigAutoField(primary_key=True)
    pilote = models.CharField(max_length=100)
    date_depart = models.DateField(blank=True, null=True)
    date_arrivee = models.DateField(blank=True, null=True)
    aeroport_arrive = models.ForeignKey(TraficaerienAeroport, models.DO_NOTHING)
    aeroport_depart = models.ForeignKey(TraficaerienAeroport, models.DO_NOTHING)
    avion = models.ForeignKey(TraficaerienAvion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'traficaerien_vol'


class Vol(models.Model):
    idvol = models.IntegerField(db_column='IdVol', primary_key=True)  # Field name made lowercase.
    idavion = models.ForeignKey(Avion, models.DO_NOTHING, db_column='IdAvion')  # Field name made lowercase.
    pilotevol = models.CharField(db_column='PiloteVol', max_length=45)  # Field name made lowercase.
    idaeroportdepart = models.ForeignKey(Aeroport, models.DO_NOTHING, db_column='IdAeroportDepart')  # Field name made lowercase.
    idaeroportarrivee = models.ForeignKey(Aeroport, models.DO_NOTHING, db_column='IdAeroportArrivee')  # Field name made lowercase.
    datedepartvol = models.DateTimeField(db_column='DateDepartVol')  # Field name made lowercase.
    datearriveevol = models.DateTimeField(db_column='DateArriveeVol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vol'
