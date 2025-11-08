from django.contrib import admin
from .models import Property
from .models import Contact


# Register your models here.
admin.site.register(Property)

admin.site.register(Contact)
