from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=200)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     joined_on = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.full_name
#
#
#
# cCATEGORIES = ((1, 'News'), (2, 'Books'), (3, 'Software'), (4, 'Web'), (5, 'Design'), (6, 'Presentation'),
#               (7, 'Educational'), (8, 'Streaming'), (9, 'Video'), (10,'Writing'), (11, 'Travel'), (12, 'Blog'),
#               (13, 'E-commerce'), (14, 'Photo Editing'), (15, 'Video Editing'), (16, 'Food & Beverages'))
#




class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(null=True)
    def __str__(self):
        return str(self.name)

# class Cart(models.Model):
#     total = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "Cart: " + str(self.id)

class CartProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)




#
# class SubscriptionPlan(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     plan_name = models.CharField(max_length=100)
#     discount = models.FloatField(default=0.00)
#     marked_price = models.FloatField(null=False, blank=False, default=0.00)
#     selling_price = models.FloatField(null=False, blank=False)
#
#
# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(null=True, blank=True, upload_to='images/')
#
# class Cart(models.Model):
#     customer = models.ForeignKey(
#         Customer, on_delete=models.SET_NULL, null=True, blank=True)
#     total = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "Cart: " + str(self.id)
#
#
# class CartProduct(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
#     rate = models.PositiveIntegerField()
#     subtotal = models.PositiveIntegerField()
#
#     def __str__(self):
#         return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)
