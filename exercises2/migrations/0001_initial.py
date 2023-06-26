# Generated by Django 3.2.19 on 2023-06-24 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('n_floors', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
                ('total_flats', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('square_meter', models.DecimalField(decimal_places=2, max_digits=10)),
                ('n_rooms', models.IntegerField()),
                ('n_bathrooms', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('letter', models.CharField(max_length=5)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises2.building')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Flat',
                'verbose_name_plural': 'Flats',
                'ordering': ['-created_at'],
            },
        ),
    ]