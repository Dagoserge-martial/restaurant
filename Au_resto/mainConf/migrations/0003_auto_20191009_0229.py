# Generated by Django 2.2.6 on 2019-10-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainConf', '0002_heure_travail_ferme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='heure_travail',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='image_slide',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='statut',
            field=models.BooleanField(default=True),
        ),
    ]