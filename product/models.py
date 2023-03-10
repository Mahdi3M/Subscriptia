from django.db import models
from accounts.models import *
from datetime import timezone

# Create your models here.

CATEGORIES = (('None', 'None'), ('News', 'News'), ('Books', 'Books'), ('Streaming', 'Streaming'),
 ('Software', 'Software'), ('Web', 'Web'), ('Design', 'Design'), ('Presentation', 'Presentation'),    ('Educational', 'Educational'), ('Streaming', 'Streaming'), ('Video', 'Video'), ('Writing',
                                                                   'Writing'), ('Travel', 'Travel'), ('Blog', 'Blog'),
 ('E-commerce', 'E-commerce'), ('Photos', 'Photo Editing'), ('Videos', 'Video Editing'), ('Music', 'Music'))


RANGE = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    slug = models.SlugField(unique=True, max_length=30)
    rating = models.PositiveIntegerField(default=0, choices=RANGE)
    rating_amount = models.PositiveBigIntegerField(default=0)
    in_wishlist = models.PositiveIntegerField(default=0)
    in_cart = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True,
                              upload_to='products/product_images/')
    plan_name = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.00)
    discount = models.FloatField(default=-0.00)
    category = models.CharField(
        max_length=200, choices=CATEGORIES, default=None)
    time_added = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f'{self.name}: {self.description}'


class BannerImg(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    banner = models.ImageField(null=True, blank=True, upload_to="products/banner_images/")

class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        unique_together = ['user', 'product']

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)


class Wishlist_Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)