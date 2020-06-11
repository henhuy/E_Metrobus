# Generated by Django 2.2.5 on 2020-06-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_metrobus', '0005_bug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='type',
            field=models.CharField(choices=[('technical', 'Technisches Problem'), ('usage', 'Schwierigkeit bei der Nutzung der App'), ('content', 'Inkorrekter oder unverständlicher Inhalt'), ('other', 'Anderes')], max_length=20, verbose_name='Problem'),
        ),
    ]
