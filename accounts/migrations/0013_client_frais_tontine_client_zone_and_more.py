# Generated by Django 4.1.7 on 2023-06-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_delete_client_inscrit'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Frais_tontine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Zone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Frais_tontine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Zone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
