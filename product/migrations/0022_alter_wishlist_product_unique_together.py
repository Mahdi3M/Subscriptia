# Generated by Django 4.1.6 on 2023-02-22 08:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0021_alter_cartproduct_product_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wishlist_product',
            unique_together={('user', 'product')},
        ),
    ]
