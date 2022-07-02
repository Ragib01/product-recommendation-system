from django.db import models
from django.utils import timezone
from django.conf import settings


class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WeatherType(models.Model):
    name = models.CharField(max_length=100)
    temp_high = models.FloatField(null=True)
    temp_low = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    LABEL = (
        ('N', 'New'),
        ('BS', 'Best Seller')
    )

    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    weather_type = models.ForeignKey(WeatherType, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    description = models.TextField(null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=5000, null=True, blank=True)
    label = models.CharField(choices=LABEL, max_length=2)
    published = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default=published)
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.item_name
