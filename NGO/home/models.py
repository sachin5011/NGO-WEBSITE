from django.db import models
from mimetypes import guess_type
class Carousel(models.Model):
    carousel_img = models.FileField(upload_to="carousel/", max_length=300, null=True)
    title = models.CharField(max_length=150, blank=True)
    sub_title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        name = str(self.carousel_img)
        return name

class About(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image1 = models.FileField(upload_to="mission/", max_length=300, blank=True)

    def __str__(self):
        return self.title

class Vision(models.Model):
    title = models.CharField(max_length=300)
    desc = models.TextField()
    image1 = models.FileField(upload_to="vision/", max_length=300, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=300, blank=True)
    designation = models.CharField(max_length=300, blank=True)
    image = models.FileField(upload_to="team/", max_length=600, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ImageCategory(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
class Gallery(models.Model):
    title = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    image = models.FileField(upload_to="gallery/", max_length=500, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email

class Address(models.Model):
    street = models.CharField(max_length=300, blank=True)
    building_no = models.CharField(max_length=300, blank=True)
    district = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=300, blank=True)
    pincode = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.state


class Services(models.Model):
    title = models.CharField(max_length=300, blank=True)
    sub_title = models.CharField(max_length=500, blank=True)
    image = models.FileField(upload_to="services/", max_length=500, blank=True)

    def __str__(self):
        return self.title


class Donate(models.Model):
    name = models.CharField(max_length=500, blank=True)
    account = models.CharField(max_length=40, blank=True)
    ifsc_code = models.CharField(max_length=40, blank=True)
    bank_name = models.CharField(max_length=150, blank=True)
    qrcode = models.FileField(upload_to="qrcode/", max_length=500, blank=True)
    upi_id = models.CharField(max_length=500, default=True)
    def __str__(self):
        return self.bank_name
