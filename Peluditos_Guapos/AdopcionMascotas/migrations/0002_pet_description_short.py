# Generated by Django 4.2.4 on 2023-09-14 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdopcionMascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description_short',
            field=models.TextField(default='', verbose_name='Breve Descripcion'),
            preserve_default=False,
        ),
    ]
