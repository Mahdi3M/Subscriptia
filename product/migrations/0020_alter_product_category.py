
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_wishlist_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('None', 'None'), ('News', 'News'), ('Books', 'Books'), ('Streaming', 'Streaming'), ('Software', 'Software'), ('Web', 'Web'), ('Design', 'Design'), ('Presentation', 'Presentation'), ('Educational', 'Educational'), ('Streaming', 'Streaming'), ('Video', 'Video'), ('Writing', 'Writing'), ('Travel', 'Travel'), ('Blog', 'Blog'), ('E-commerce', 'E-commerce'), ('Photos', 'Photo Editing'), ('Videos', 'Video Editing'), ('Music', 'Music')], default=None, max_length=200),
        ),
    ]
