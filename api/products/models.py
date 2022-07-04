from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductType, self).save(*args, **kwargs)

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

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    weather_type = models.ForeignKey(WeatherType, on_delete=models.PROTECT, default=1)
    item_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    description = models.TextField(null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='static/products', blank=True, max_length=500)
    stock = models.BigIntegerField(default=10)
    label = models.CharField(choices=LABEL, max_length=2)
    published = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=100, choices=options, default=published)
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.item_name
