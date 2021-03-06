# Generated by Django 4.0.5 on 2022-07-03 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('temp_high', models.FloatField(null=True)),
                ('temp_low', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='static/products')),
                ('stock', models.BigIntegerField(default=10)),
                ('label', models.CharField(choices=[('N', 'New'), ('BS', 'Best Seller')], max_length=2)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default=models.DateTimeField(default=django.utils.timezone.now), max_length=10)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producttype')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
