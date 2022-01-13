# Generated by Django 4.0.1 on 2022-01-13 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0002_userstory_rename_bio_myclubuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='desire',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='reason',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='who',
            field=models.TextField(),
        ),
    ]
