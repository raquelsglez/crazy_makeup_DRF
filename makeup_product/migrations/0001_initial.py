# Generated by Django 3.2.19 on 2023-05-09 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MakeupProduct',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stock', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('trademark', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'MakeupProduct',
                'verbose_name_plural': 'MakeupProducts',
            },
        ),
    ]