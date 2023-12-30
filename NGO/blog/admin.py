from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "timestamp", "image", "content")


"""registering Blog to admin dashboard"""
admin.site.register(Blog, BlogAdmin)
