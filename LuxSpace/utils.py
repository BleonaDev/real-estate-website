from .models import Property
from django.db.models import Q

def search_properties(query):
    return Property.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(location__icontains=query)
    )
