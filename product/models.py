from django.db import models

# Create your models here.

CATEGORIES = ((0, 'None'), (1, 'News'), (2, 'Books'), (3, 'Software'), (4, 'Web'), (5, 'Design'), (6, 'Presentation'),
              (7, 'Educational'), (8, 'Streaming'), (9, 'Video'), (10,'Writing'), (11, 'Travel'), (12, 'Blog'), 
              (13, 'E-commerce'), (14, 'Photo Editing'), (15, 'Video Editing'), (16, 'Food & Beverages'))


VALID_RATINGS = (('z', 0), ('o', 1), ('tw', 2), ('th', 3), ('fo', 4), ('fi', 5))


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    slug = models.SlugField(unique=True, auto_created=True)
    rating = models.PositiveIntegerField(choices=VALID_RATINGS, default=0)
    review = models.CharField(max_length=500, default="")
    in_wishlist = models.PositiveIntegerField(default=0)
    in_cart = models.PositiveIntegerField(default=0)
    banner = models.ImageField(null=True, blank=True, upload_to='products/banner/')
    image = models.ImageField(null=True, blank=True, upload_to='products/product_images/')
    plan_name = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    category = models.CharField(max_length=200, choices=CATEGORIES, default='None')

    def __str__(self):
        return f'{self.name}: {self.description}'