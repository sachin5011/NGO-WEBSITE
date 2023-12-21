
from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/about-us/', views.aboutus, name="aboutus"),
    path('home/services/', views.services, name='services'),
    path('home/gallery/', views.gallery, name='gallery'),
    path('home/blog-post/', views.blog, name='blog'),
    path('home/contact-us/', views.contactus, name='contactus'),
]
