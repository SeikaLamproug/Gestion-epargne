# Generated by Django 4.1.7 on 2023-06-06 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_email_remove_profile_telephone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='CNI',
            new_name='cni',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='CNI_garant',
            new_name='cni_garant',
        ),
    ]
