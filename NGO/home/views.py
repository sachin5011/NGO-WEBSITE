from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, "about_us.html")

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    return render(request, "blog.html")

def contactus(request):
    return render(request, "contact_us.html")

