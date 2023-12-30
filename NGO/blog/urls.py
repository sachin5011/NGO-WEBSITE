from django.urls import path
from blog import views



urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-post-details/<int:pk>/', views.blog_details, name='blogdetails'),

]