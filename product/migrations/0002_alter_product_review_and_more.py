# Generated by Django 4.1.6 on 2023-02-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='selling_price',
            field=models.FloatField(),
        ),
    ]