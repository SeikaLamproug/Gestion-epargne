# Generated by Django 4.2.2 on 2023-06-16 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_payement_debut_payement_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='payement',
            name='montant_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]