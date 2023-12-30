from django.contrib import admin
from .models import Carousel, About, Mission, Vision, Team, ImageCategory, Gallery, Contact, Address, Services, Donate


class CarouselAdmin(admin.ModelAdmin):
    list_display = ("carousel_img", "title", "sub_title")


class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "desc")

class MissionAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "image1")

class VisionAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "image1")


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "image")

class ImageCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "image")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "building_no", "district", "state",
                    "pincode", "phone", "email")

class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "image")

class DonateAdmin(admin.ModelAdmin):
    list_display = ("bank_name", "name", "account", "ifsc_code", "upi_id", "qrcode")


'''registering Carousel model to Admin'''
admin.site.register(Carousel, CarouselAdmin)
'''registering About model to Admin'''
admin.site.register(About, AboutAdmin)
'''registering Mission model to Admin'''
admin.site.register(Mission, MissionAdmin)
'''registering Vision model to Admin'''
admin.site.register(Vision, VisionAdmin)
'''registering Team model to Admin'''
admin.site.register(Team, TeamAdmin)
'''registering ImageCategory model to Admin'''
admin.site.register(ImageCategory, ImageCategoryAdmin)
'''registering Gallery model to Admin'''
admin.site.register(Gallery, GalleryAdmin)
'''registering Contact model to Admin'''
admin.site.register(Contact, ContactAdmin)
'''registering Address model to Admin'''
admin.site.register(Address, AddressAdmin)
'''registering Services model to Admin'''
admin.site.register(Services, ServicesAdmin)
'''registering Donate model to Admin'''
admin.site.register(Donate, DonateAdmin)
