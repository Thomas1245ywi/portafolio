# Generated by Django 4.2.5 on 2023-09-13 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CajaMascotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptbox',
            name='box_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
