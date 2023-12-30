from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.FileField(upload_to="blog/", max_length=500, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title



