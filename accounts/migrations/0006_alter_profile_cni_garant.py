# Generated by Django 4.1.7 on 2023-06-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_auth_token_remove_profile_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='CNI_garant',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
