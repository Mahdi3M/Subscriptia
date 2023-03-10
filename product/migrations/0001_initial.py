# Generated by Django 4.1.6 on 2023-02-16 11:18

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('rating', models.PositiveIntegerField()),
                ('review', models.CharField(max_length=500)),
                ('is_wishlist', models.BooleanField(default=False)),
                ('is_cart', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('discount', models.FloatField(default=0.0)),
                ('marked_price', models.FloatField(default=0.0)),
                ('selling_price', models.FloatField(default=models.FloatField(default=0.0))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(1, 'News'), (2, 'Books'), (3, 'Software'), (4, 'Web'), (5, 'Design'), (6, 'Presentation'), (7, 'Educational'), (8, 'Streaming'), (9, 'Video'), (10, 'Writing'), (11, 'Travel'), (12, 'Blog'), (13, 'E-commerce'), (14, 'Photo Editing'), (15, 'Video Editing'), (16, 'Food & Beverages')], max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
