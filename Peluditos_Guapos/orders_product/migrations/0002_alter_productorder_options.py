
# Generated by Django 5.0.2 on 2024-04-04 14:59

# Generated by Django 5.0.1 on 2024-04-04 17:03


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productorder',
            options={'ordering': ['id'], 'verbose_name': 'Pedidos Producto', 'verbose_name_plural': 'Pedidos Producto'},
        ),
    ]
