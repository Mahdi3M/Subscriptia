from django.db import models

# Create your models here.

CATEGORIES = ((1, 'News'), (2, 'Books'), (3, 'Software'), (4, 'Web'), (5, 'Design'), (6, 'Presentation'),
              (7, 'Educational'), (8, 'Streaming'), (9, 'Video'), (10,'Writing'), (11, 'Travel'), (12, 'Blog'), 
              (13, 'E-commerce'), (14, 'Photo Editing'), (15, 'Video Editing'), (16, 'Food & Beverages'))


def validate_even(value):
    if value not in range(0, 6):
        raise ValidationError(
            _('%(value) is not a valid rating'), 
            params={'value': value},
        )
    


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    rating = models.PositiveIntegerField(
        validators=[validate_even]
    )
    review = models.CharField(max_length=500, default="")
    is_wishlist = models.BooleanField(default=False)
    is_cart = models.BooleanField(default=False)


class Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length= 30,choices=CATEGORIES)


class SubscriptionPlan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    discount = models.FloatField(default=0.00)
    marked_price = models.FloatField(null=False, blank=False, default=0.00)
    selling_price = models.FloatField(null=False, blank=False)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
