# Generated by Django 4.1.7 on 2023-02-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='subscriptionplan',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_cart',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_wishlist',
        ),
        migrations.AddField(
            model_name='product',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='products/banner/'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(0, 'None'), (1, 'News'), (2, 'Books'), (3, 'Software'), (4, 'Web'), (5, 'Design'), (6, 'Presentation'), (7, 'Educational'), (8, 'Streaming'), (9, 'Video'), (10, 'Writing'), (11, 'Travel'), (12, 'Blog'), (13, 'E-commerce'), (14, 'Photo Editing'), (15, 'Video Editing'), (16, 'Food & Beverages')], default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_cart',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='in_wishlist',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='plan_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(choices=[('z', 0), ('o', 1), ('tw', 2), ('th', 3), ('fo', 4), ('fi', 5)], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='SubscriptionPlan',
        ),
    ]
