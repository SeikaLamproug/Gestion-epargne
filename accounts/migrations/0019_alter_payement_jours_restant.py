# Generated by Django 4.2.2 on 2023-06-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_payement_compte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payement',
            name='jours_restant',
            field=models.IntegerField(blank=True, default=31),
        ),
    ]
