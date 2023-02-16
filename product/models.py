from django.db import models

# Create your models here.

CATEGORIES = ('News', 'Books', 'Software', 'Web', 'Design', 'Presentation',
              'Educational', 'Streaming', 'Video', 'Writing', 'Travel', 'Blog', 
              'E-commerce', 'Photo Editing', 'Video Editing', 'Food & Beverages')


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    review = models.CharField(max_length=500)
    is_wishlist = models.BooleanField(default=False)
    is_cart = models.BooleanField(default=False)


class Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORIES)


class SubscriptionPlan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    discount = models.FloatField(default=0.00)
    marked_price = models.FloatField(null=False, blank=False, default=0.00)
    selling_price = marked_price - (discount/100)*marked_price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
