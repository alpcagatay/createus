# Generated by Django 3.2.11 on 2022-01-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_user_rookie'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='numberofdislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstory',
            name='numberoflikes',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
