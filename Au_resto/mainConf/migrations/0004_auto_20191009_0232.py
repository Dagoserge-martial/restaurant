# Generated by Django 2.2.6 on 2019-10-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainConf', '0003_auto_20191009_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heure_travail',
            name='heure_debut',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='heure_travail',
            name='heure_fin',
            field=models.TimeField(blank=True),
        ),
    ]
