# Generated by Django 4.0.5 on 2022-07-03 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weather_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.weathertype'),
        ),
    ]
