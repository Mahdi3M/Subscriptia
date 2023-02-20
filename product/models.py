from django.db import models
from accounts.models import *

# Create your models here.

CATEGORIES = (('None', 'None'), ('News', 'News'), ('Books', 'Books'), ('Streaming', 'Streaming'),)
# ('software', 'Software'), ('web', 'Web'), ('design', 'Design'), ('presentation', 'Presentation'),
#               ('educational', 'Educational'), ('streaming', 'Streaming'), ('video', 'Video'), ('writing',
#                                                                    'Writing'), ('travel', 'Travel'), ('blog', 'Blog'),
#               ('e-commerce', 'E-commerce'), ('photos', 'Photo Editing'), ('videos', 'Video Editing'), ('food', 'Food & Beverages')


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    slug = models.SlugField(unique=True, max_length=30)
    rating = models.PositiveIntegerField(default=0)
    in_wishlist = models.PositiveIntegerField(default=0)
    in_cart = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True,
                              upload_to='products/product_images/')
    plan_name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=-0.00)
    category = models.CharField(
        max_length=200, choices=CATEGORIES, default=None)

    def __str__(self):
        return f'{self.name}: {self.description}'


class BannerImg(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    banner = models.ImageField(null=True, blank=True, upload_to="products/banner_images/")


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=0)

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, blank=True, null=True)