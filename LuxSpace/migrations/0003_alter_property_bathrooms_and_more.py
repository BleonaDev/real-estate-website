# Generated by Django 5.1.7 on 2025-04-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LuxSpace', '0002_alter_property_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_size_acres',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='square_feet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='property_gallery/'),
        ),
    ]
