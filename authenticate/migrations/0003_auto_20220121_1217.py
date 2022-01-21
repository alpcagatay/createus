# Generated by Django 3.2.11 on 2022-01-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_userstory_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='userstory',
            name='project',
        ),
        migrations.AddField(
            model_name='userstory',
            name='category',
            field=models.CharField(default='Category1', max_length=255),
        ),
    ]