# Generated by Django 4.0.5 on 2022-06-08 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aeroport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='avion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='compagnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('pays_de_rattachement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='type_avion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('longueur_piste_necessaire', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilote', models.CharField(max_length=100)),
                ('date_depart', models.DateField(blank=True, null=True)),
                ('date_arrivee', models.DateField(blank=True, null=True)),
                ('aeroport_arrive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivee', to='traficaerien.aeroport')),
                ('aeroport_depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='traficaerien.aeroport')),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traficaerien.avion')),
            ],
        ),
        migrations.CreateModel(
            name='piste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longeur', models.IntegerField()),
                ('aeroport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traficaerien.aeroport')),
            ],
        ),
        migrations.AddField(
            model_name='avion',
            name='compagnie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traficaerien.compagnie'),
        ),
        migrations.AddField(
            model_name='avion',
            name='modele',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traficaerien.type_avion'),
        ),
    ]
