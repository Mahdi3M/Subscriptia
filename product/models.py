from django.db import models

# Create your models here.

CATEGORIES = (('None', 'None'), ('News', 'News'), ('Books', 'Books'), ('Streaming', 'Streaming'),
 ('Software', 'Software'), ('Web', 'Web'), ('Design', 'Design'), ('Presentation', 'Presentation'),    ('Educational', 'Educational'), ('Streaming', 'Streaming'), ('Video', 'Video'), ('Writing',
                                                                   'Writing'), ('Travel', 'Travel'), ('Blog', 'Blog'),
 ('E-commerce', 'E-commerce'), ('Photos', 'Photo Editing'), ('Videos', 'Video Editing'), ('Music', 'Music'))


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