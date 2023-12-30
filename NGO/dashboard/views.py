import os
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import Carousel, About, Mission, Vision, Services, Team, Gallery, Donate
from blog.models import Blog
from .models import Payments
from django.contrib.auth.models import User
from django.utils import timezone


"""DASHBOARD HOME PAGE"""
@login_required
def dashboard(request):
    obj = Payments.objects.all().order_by('-id')
    paginator = Paginator(obj, 11)
    page_number = request.GET.get('page')
    pay_obj = paginator.get_page(page_number)
    total_pages = pay_obj.paginator.num_pages

    totla_number_of_donation = obj.count()
    total_amount = Payments.objects.aggregate(Sum('pay_amount'))

    context = {
        'pay_obj': pay_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)],
        'totla_number_of_donation': totla_number_of_donation,
        'total_amount': total_amount['pay_amount__sum']
    }
    return render(request, "dashboard/index.html", context=context)


"""CAROUSEL HOME PAGE"""
@login_required
def dashboardhomeedit(request):

    obj = Carousel.objects.all().order_by('-id')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    carousel_obj = paginator.get_page(page_number)
    total_pages = carousel_obj.paginator.num_pages

    context = {
        'carousel_obj': carousel_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }

    return render(request, 'dashboard/dashboard-carousel.html', context=context)

"""CAROUSEL EDIT PAGE"""
@login_required
def dashboardhomeeditcarousel(request, pk):
    edit_obj = Carousel.objects.get(pk=pk)

    if request.method == 'POST':
        # print(request.FILES['upload'])
        if len(request.FILES) != 0:
            if len(edit_obj.carousel_img) > 0:
                os.remove(edit_obj.carousel_img.path)
            edit_obj.carousel_img = request.FILES['upload']
        edit_obj.title = request.POST['title']
        edit_obj.sub_title = request.POST['sub_title']

        edit_obj.save()
        return redirect('dashboardhome')

    context = {
        'edit_obj': edit_obj
    }
    return render(request, 'dashboard/carousel-edit.html', context=context)


"""CAROUSEL DELETE PAGE"""
@login_required
def dashboardhomedeletecarousel(request, pk):

    del_obj = Carousel.objects.get(pk=pk)
    del_obj.delete()

    return redirect('dashboardhome')

"""ABOUT HOME PAGE"""
@login_required
def dashboardaboutedit(request):
    """getting all about data from db"""
    obj = About.objects.all().order_by("-id")
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    abt_obj = paginator.get_page(page_number)
    total_pages = abt_obj.paginator.num_pages

    context = {
        'abt_obj': abt_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }

    return render(request, 'dashboard/dashboard-about.html', context=context)

"""ABOUT EDIT PAGE"""
@login_required
def dashboardabouteditpage(request, pk):

    """getting all about data from db"""
    abt_obj = About.objects.filter(id=pk).first()

    context = {
        'abt_obj': abt_obj
    }

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['sub_title']

        abt_obj.title = title
        abt_obj.desc = desc

        abt_obj.save()
        return redirect('dashboardabout')

    return render(request, 'dashboard/about-edit.html', context=context)

"""ABOUT DELETE PAGE"""
@login_required
def dashboardaboutdeletepage(request, pk):

    del_obj = About.objects.get(pk=pk)
    del_obj.delete()
    return redirect('dashboardabout')

"""MISSION HOME PAGE"""
@login_required
def dashboardmissionedit(request):

    """getting all mission data from db"""
    obj = Mission.objects.all().order_by("-id")
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    mission_obj = paginator.get_page(page_number)
    total_pages = mission_obj.paginator.num_pages

    context = {
        'mission_obj': mission_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }

    return render(request, 'dashboard/dashboard-mission.html', context=context)

"""MISSION EDIT PAGE"""
@login_required
def dashboardmissioneditpage(request, pk):

    mission_obj = Mission.objects.get(pk=pk)

    context = {
        'mission_obj': mission_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(mission_obj.image1) > 0:
                os.remove(mission_obj.image1.path)
            mission_obj.image1 = request.FILES['upload']
        mission_obj.title = request.POST['title']
        mission_obj.desc = request.POST['desc']

        mission_obj.save()
        return redirect('dashboardmission')

    return render(request, 'dashboard/mission-edit.html', context=context)

"""MISSION DELETE PAGE"""
@login_required
def dashboardmissiondeletepage(request, pk):
    del_obj = Mission.objects.get(pk=pk)
    del_obj.delete()
    return redirect('dashboardmission')

"""VISION HOME PAGE """
@login_required
def dashboardvisionedit(request):

    """getting all vision data from db"""
    obj = Vision.objects.all().order_by("-id")
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    vision_obj = paginator.get_page(page_number)
    total_pages = vision_obj.paginator.num_pages

    context = {
        'vision_obj': vision_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }

    return render(request, 'dashboard/dashboard-vision.html', context=context)

"""VISION EDIT PAGE """
@login_required
def dashboardvisioneditpage(request, pk):
    vision_obj = Vision.objects.get(pk=pk)

    context = {
        'vision_obj': vision_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(vision_obj.image1) > 0:
                os.remove(vision_obj.image1.path)
            vision_obj.image1 = request.FILES['upload']
        vision_obj.title = request.POST['title']
        vision_obj.desc = request.POST['desc']

        vision_obj.save()
        return redirect('dashboardvision')

    return render(request, 'dashboard/vision-edit.html', context=context)


"""VISION DELETE PAGE """
@login_required
def dashboardvisiondeletepage(request, pk):
    del_obj = Vision.objects.get(pk=pk)
    del_obj.delete()

    return redirect('dashboardvision')

"""SERVICE HOME PAGE"""
@login_required
def dashboardserviceedit(request):

    obj = Services.objects.all().order_by('-id')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    serv_obj = paginator.get_page(page_number)
    total_pages = serv_obj.paginator.num_pages

    context = {
        'serv_obj': serv_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'dashboard/dashboard-service.html', context=context)

"""SERVICE EDIT PAGE"""
@login_required
def dashboardserviceeditpage(request, pk):

    serv_obj = Services.objects.get(pk=pk)

    context = {
        'serv_obj': serv_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(serv_obj.image) > 0:
                os.remove(serv_obj.image.path)
            serv_obj.image = request.FILES['upload']
        serv_obj.title = request.POST['title']
        serv_obj.sub_title = request.POST['desc']
        serv_obj.save()
        return redirect('dashboardservice')
    return render(request, 'dashboard/service-edit.html', context=context)


"""SERVICE DELETE PAGE"""
@login_required
def dashboardservicedeletepage(request, pk):
    del_obj = Services.objects.get(pk=pk)
    del_obj.delete()

    return redirect('dashboardservice')

"""TEAM HOME PAGE"""
@login_required
def dashboardteamedit(request):

    obj = Team.objects.all().order_by('-id')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    team_obj = paginator.get_page(page_number)
    total_pages = team_obj.paginator.num_pages

    context = {
        'team_obj': team_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'dashboard/dashboard-team.html', context=context)

"""TEAM EDIT PAGE"""
@login_required
def dashboardteameditpage(request, pk):

    team_obj = Team.objects.get(pk=pk)

    context = {
        'team_obj': team_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(team_obj.image) > 0:
                os.remove(team_obj.image.path)
            team_obj.image = request.FILES['upload']
        team_obj.name = request.POST['name']
        team_obj.designation = request.POST['designation']
        team_obj.about = request.POST['about']

        team_obj.save()
        return redirect('dashboardteam')
    return render(request, 'dashboard/team-edit.html', context=context)

"""TEAM DELETE PAGE"""
@login_required
def dashboardteamdeletepage(request, pk):

    del_obj = Team.objects.get(pk=pk)
    del_obj.delete()

    return redirect('dashboardteam')

"""GALLERY HOME PAGE"""
@login_required
def dashboardgalleryedit(request):

    obj = Gallery.objects.all().order_by('-id')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    gallery_obj = paginator.get_page(page_number)
    total_pages = gallery_obj.paginator.num_pages

    context = {
        'gallery_obj': gallery_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'dashboard/dashboard-gallery.html', context=context)

"""GALLERY EDIT PAGE"""
@login_required
def dashboardgalleryeditpage(request, pk):

    gallery_obj = Gallery.objects.get(pk=pk)

    context = {
        'gallery_obj': gallery_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(gallery_obj.image) > 0:
                os.remove(gallery_obj.image.path)
            gallery_obj.image = request.FILES['upload']
        gallery_obj.title = request.POST['title']
        gallery_obj.category = request.POST['category']


        gallery_obj.save()
        return redirect('dashboardgallery')
    return render(request, 'dashboard/gallery-edit.html', context=context)

"""GALLERY DELETE PAGE"""
@login_required
def dashboardgallerydeletepage(request, pk):

    del_obj = Gallery.objects.get(pk=pk)
    del_obj.delete()
    return redirect('dashboardgallery')

"""BLOG HOME PAGE"""
@login_required
def dashboardblogedit(request):

    obj = Blog.objects.all().order_by('-id')
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    total_pages = blog_obj.paginator.num_pages

    context = {
        'blog_obj': blog_obj,
        'last_pages': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'dashboard/dashboard-blog.html', context=context)

"""BLOG EDIT PAGE"""
@login_required
def dashboardblogeditpage(request, pk):

    blog_obj = Blog.objects.get(pk=pk)

    context = {
        'blog_obj': blog_obj
    }

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(blog_obj.image) > 0:
                os.remove(blog_obj.image.path)
            blog_obj.image = request.FILES['upload']
        blog_obj.title = request.POST['title']
        blog_obj.content = request.POST['content']

        blog_obj.save()
        return redirect('dashboardblog')
    return render(request, 'dashboard/blog-edit.html', context=context)

"""BLOG DELETE PAGE"""
@login_required
def dashboardblogdeletepage(request, pk):

    del_obj = Blog.objects.get(pk=pk)
    del_obj.delete()

    return redirect('dashboardblog')

"""CHANGE PASSWORD"""
@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old-pass']
        new_pass = request.POST['new-pass']
        repeat_pass = request.POST['rpt-pass']
        if old_password and new_pass and repeat_pass:
            user_obj = User.objects.get(username__exact=request.user)
            if user_obj.check_password(old_password):
                user_obj.set_password(new_pass)
                user_obj.save()
                return redirect('dashboard')
    return render(request, 'dashboard/password-change.html')
@login_required
def view_all_users(request):

    user_obj = User.objects.all().order_by('-id')

    context = {
        'user_obj': user_obj
    }
    return render(request, 'dashboard/view-users.html', context=context)

@login_required
def delete_user(request, pk):
    del_user = User.objects.get(pk=pk)
    del_user.delete()
    return redirect('allusers')

def add_carousel(request):
    if request.method == 'POST':
        title = request.POST['title']
        sub_title = request.POST['sub-title']
        image = request.FILES('upload')

        obj = Carousel(title=title, sub_title=sub_title, carousel_img=image)
        obj.save()

    return render(request, 'dashboard/add-carousel.html')

def add_about(request):

    if request.method == 'POST':
        title = request.POST['title']
        sub_title = request.POST['sub-title']

        abt = About(title=title, desc=sub_title)
        abt.save()

    return render(request, 'dashboard/add-about.html')

def add_mission(request):

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES['upload']

        miss = Mission(title=title, desc=desc, image1=image)
        miss.save()

    return render(request, 'dashboard/add-mission.html')
def add_vision(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES['upload']

        vis = Vision(title=title, desc=desc, image1=image)
        vis.save()

    return render(request, 'dashboard/add-vision.html')
def add_service(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        image = request.FILES['upload']

        ser = Services(title=title, sub_title=desc, image=image)
        ser.save()

    return render(request, 'dashboard/add-service.html')
def add_team(request):

    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        about = request.POST['about']
        image = request.FILES['upload']

        team = Team(name=name, designation=designation, about=about, image=image)
        team.save()

    return render(request, 'dashboard/add-team.html')
def add_blog(request):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        image = request.FILES['upload']
        timestamp = timezone.now()

        blog = Blog(title=title, content=content, author=author,image=image, timestamp=timestamp)
        blog.save()

    return render(request, 'dashboard/add-blog.html')

def add_gallery(request):

    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['upload']

        gall = Gallery(title=title, image=image)
        gall.save()

    return render(request, 'dashboard/add-gallery.html')
def add_payment(request):

    if request.method == 'POST':
        bnk_name = request.POST['name']
        holder_name = request.POST['holder-name']
        acc_no = request.POST['acc-no']
        ifsc_code = request.POST['ifsc']
        upi_id = request.POST['upi-id']
        image = request.FILES['upload']

        donate = Donate(name=holder_name, account=acc_no, ifsc_code=ifsc_code,
                        bank_name=bnk_name, upi_id=upi_id, qrcode=image)
        donate.save()

    return render(request, 'dashboard/add-payment.html')