# Generated by Django 3.2.11 on 2022-01-21 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=96, null=True, verbose_name='Email address')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super user')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/profile/', verbose_name='Profile picture')),
                ('role', models.TextField(blank=True, null=True, verbose_name='role')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.TextField(default='As')),
                ('second', models.TextField(default='I would like to')),
                ('who', models.TextField()),
                ('third', models.TextField(default='so that I can')),
                ('desire', models.TextField()),
                ('reason', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
