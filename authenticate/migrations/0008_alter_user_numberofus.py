# Generated by Django 3.2.11 on 2022-01-21 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_user_numberofus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='numberofus',
            field=models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='numberofus'),
        ),
    ]
