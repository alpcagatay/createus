# Generated by Django 3.2.11 on 2022-01-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0008_alter_user_numberofus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rookie',
            field=models.TextField(blank=True, null=True, verbose_name='rookie'),
        ),
    ]
