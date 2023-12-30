from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add-user/', views.add_more_users, name='adduser')
]