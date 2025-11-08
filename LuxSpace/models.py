from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100 , null=True, blank=True)
    price = models.TextField( null=True, blank=True)
    carousel_image1 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    carousel_image2 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    carousel_image3 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    carousel_image4 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    main_image = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    bedrooms = models.TextField(null=True, blank=True)
    bathrooms = models.TextField(null=True, blank=True)
    square_feet = models.TextField(null=True, blank=True)
    lot_size_acres = models.TextField (null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    full_description = models.TextField( null=True, blank=True)
    map_embed_url = models.TextField( max_length=500, null=True, blank=True)
    photo1 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image1 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image2 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image3 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image4 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image5 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image6 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image7 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image8 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image9 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image10 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image11 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image12 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    image13 = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True, null=True)
    icon1 = models.CharField(max_length=100 , blank=True, null=True)
    text1 = models.TextField(max_length=100 , blank=True, null=True)
    icon2 = models.CharField(max_length=100 , blank=True, null=True)
    text2 = models.TextField(max_length=100 , blank=True, null=True)
    icon3 = models.CharField(max_length=100 , blank=True, null=True)
    text3 = models.TextField(max_length=100 , blank=True, null=True)
    icon4 = models.CharField(max_length=100 , blank=True, null=True)
    text4 = models.TextField(max_length=100 , blank=True, null=True)
    icon5 = models.CharField(max_length=100 , blank=True, null=True)
    text5 = models.TextField(max_length=100 , blank=True, null=True)
    old_price = models.CharField(max_length=100 , null=True, blank=True)


    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name









    # Create your models here.
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py runserver
    # python manage.py createsuperuser

