# Generated by Django 5.1.7 on 2025-04-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuxSpace', '0005_property_photo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='map_embed_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
