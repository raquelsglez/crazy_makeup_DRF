# Generated by Django 3.2.19 on 2023-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20230606_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nevera',
            name='marca',
            field=models.CharField(default='Marca', max_length=100),
        ),
        migrations.AlterField(
            model_name='nevera',
            name='nombre',
            field=models.CharField(default='Proof', max_length=100),
        ),
    ]
