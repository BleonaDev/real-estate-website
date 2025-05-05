# Create your views here.
# LuxSpace/views.py
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .utils import search_properties
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect

def home(request):
    properties = Property.objects.all()
    return render(request, 'build.html', {'properties': properties})
def search_view(request):
    query = request.GET.get('q', '')
    results = search_properties(query) if query else []
    paginator = Paginator(results, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_results.html', {'page_obj': page_obj, 'query': query})
def properties(request):
    properties =Property.objects.all()
    context = {'properties':properties}
    return render(request, 'properties.html', context)
def properties_view(request):
    properties = Property.objects.all()

    price_range = request.GET.get('price')
    location = request.GET.get('location')
    prop_type = request.GET.get('type')

    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
        properties = properties.filter(price__gte=min_price, price__lte=max_price)

    if location:
        properties = properties.filter(location__iexact=location)

    if prop_type:
        properties = properties.filter(property_type__iexact=prop_type)

    return render(request, 'properties.html', {'properties': properties})
def deals(request):
    property_8 = Property.objects.get(id=8)
    property_7 = Property.objects.get(id=7)
    property_9 = Property.objects.get(id=9)
    properties = [property_8, property_7, property_9]
    context = {'properties': properties}
    return render(request, 'deals.html', context)
def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})
def contact(request):
    return render(request, 'contact.html')

def login_view(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Please fill in the blank spaces")
            return redirect("login")


        if not User.objects.filter(username=email).exists():
            messages.error(request, "This email is not registered. Please create an account.")
            return redirect("register")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("home")
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return redirect("login")

    return render(request , "login.html")


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("name")
        last_name = request.POST.get("last-name")
        phone = request.POST.get("phone")

        if not (email and password and first_name and last_name):
            messages.error(request, "Please fill in all required fields.")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("register")

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            messages.success(
                request, "Account created successfully! You can now log in."
            )
            return redirect("login")

        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect("register")

    return render(request, "register.html")

def contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Ruaj të dhënat në databaze
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message,
        )
        return redirect("contact/")  # Redirect për sukses

    return render(request, "contact.html")