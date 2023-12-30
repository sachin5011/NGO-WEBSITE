
from django.urls import path
from home import views



urlpatterns = [
    path('', views.home, name="home"),
    path('home/about-us/', views.aboutus, name="aboutus"),
    path('home/services/', views.services, name='services'),
    path('home/gallery/', views.gallery, name='gallery'),
    path('home/contact-us/', views.contactus, name='contactus'),
    path('test/', views.test, name='test'),
    path('home/team/', views.team, name='teams'),
    path('home/team-details-card/<int:pk>', views.teamdetailscard, name='teamdetailscard'),
    path('home/donate-us/', views.donateus, name='donateus'),
]