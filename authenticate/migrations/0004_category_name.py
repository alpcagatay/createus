# Generated by Django 3.2.11 on 2022-01-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20220121_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
