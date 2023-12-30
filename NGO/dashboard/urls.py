
from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home-edit/', views.dashboardhomeedit, name='dashboardhome'),
    path('home-edit/edit/<int:pk>/', views.dashboardhomeeditcarousel, name='homeedit'),
    path('home-edit/delete/<int:pk>/', views.dashboardhomedeletecarousel, name='homedelete'),
    path('about-edit/', views.dashboardaboutedit, name='dashboardabout'),
    path('about-edit/edit/<int:pk>/', views.dashboardabouteditpage, name='aboutedit'),
    path('about-edit/delete//<int:pk>/', views.dashboardaboutdeletepage, name='aboutdelete'),
    path('mission-edit/', views.dashboardmissionedit, name='dashboardmission'),
    path('mission-edit/edit/<int:pk>/', views.dashboardmissioneditpage, name='missionedit'),
    path('mission-edit/delete/<int:pk>/', views.dashboardmissiondeletepage, name='missiondelete'),
    path('vision-edit/', views.dashboardvisionedit, name='dashboardvision'),
    path('vision-edit/edit/<int:pk>/', views.dashboardvisioneditpage, name='visionedit'),
    path('vision-edit/delete/<int:pk>/', views.dashboardvisiondeletepage, name='visiondelete'),
    path('service-edit/', views.dashboardserviceedit, name='dashboardservice'),
    path('service-edit/edit/<int:pk>/', views.dashboardserviceeditpage, name='serviceedit'),
    path('service-edit/delete/<int:pk>/', views.dashboardservicedeletepage, name='servicedelete'),
    path('team-edit/', views.dashboardteamedit, name='dashboardteam'),
    path('team-edit/edit/<int:pk>/', views.dashboardteameditpage, name='teamedit'),
    path('team-edit/delete/<int:pk>/', views.dashboardteamdeletepage, name='teamdelete'),
    path('gallery-edit/', views.dashboardgalleryedit, name='dashboardgallery'),
    path('gallery-edit/edit/<int:pk>/', views.dashboardgalleryeditpage, name='galleryedit'),
    path('gallery-edit/delete/<int:pk>/', views.dashboardgallerydeletepage, name='gallerydelete'),
    path('blog-edit/', views.dashboardblogedit, name='dashboardblog'),
    path('blog-edit/edit/<int:pk>/', views.dashboardblogeditpage, name='blogedit'),
    path('blog-edit/delete/<int:pk>/', views.dashboardblogdeletepage, name='blogdelete'),
    path('change-password/', views.change_password, name='password'),
    path('view-all-users/', views.view_all_users, name='allusers'),
    path('view-all-users/delete/<int:pk>/', views.delete_user, name='userdelete'),
    path('add-carousel/', views.add_carousel, name='addcarousel'),
    path('add-about/', views.add_about, name='addabout'),
    path('add-mission/', views.add_mission, name='addmission'),
    path('add-vision/', views.add_vision, name='addvision'),
    path('add-service/', views.add_service, name='addservice'),
    path('add-team/', views.add_team, name='addteam'),
    path('add-blog/', views.add_blog, name='addblog'),
    path('add-payment/', views.add_payment, name='addpayment'),
    path('add-gallery/', views.add_gallery, name='addgallery'),
]