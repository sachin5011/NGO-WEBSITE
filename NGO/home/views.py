from django.shortcuts import render
from .models import Carousel, About, Mission, Vision, Team, Gallery, Contact, Address, Services, Donate
from blog.models import Blog
from .utils import receive_email_from_client
from django.core.paginator import Paginator
from dashboard.models import Payments

def home(request):
    """taking the only lates 3 images from the database"""
    carousel_obj = Carousel.objects.all()[:3]
    """getting the latest about object"""
    about_obj = About.objects.all()
    """getting the latest mission object"""
    mission_obj = Mission.objects.all()
    """getting the latest vision object"""
    vision_obj = Vision.objects.all()
    """getting the latest causes object"""
    service_obj = Services.objects.all().order_by("-id")[:3]
    """getting the team member details"""
    team_obj = Team.objects.all()[:4]
    """getting the blog member details"""
    blog_obj = Blog.objects.all()[:3]

    for data in carousel_obj:
        print(data)


    context = {
        'carousel_obj': carousel_obj,
        'about_obj': about_obj,
        'mission_obj': mission_obj,
        'vision_obj': vision_obj,
        'service_obj': service_obj,
        'team_obj': team_obj,
        'blog_obj': blog_obj
    }

    return render(request, 'index.html', context)

def test(request):
    home_obj = Carousel.objects.all().order_by("-id")
    for img in home_obj:
        print(img)

    context = {
        'home_obj': home_obj
    }
    return render(request, 'test.html', context=context)

def aboutus(request):
    try:
        """getting the latest about object"""
        about_obj = About.objects.all()
        """getting the latest mission object"""
        mission_obj = Mission.objects.all()
        """getting the latest vision object"""
        vision_obj = Vision.objects.all()

        context = {
            'about_obj': about_obj,
            'mission_obj': mission_obj,
            'vision_obj': vision_obj
        }
    except:
        return render(request, "404.html")
    return render(request, "about_us.html", context=context)

def services(request):

    obj = Services.objects.all().order_by('-id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    service_obj = paginator.get_page(page_number)
    total_pages = service_obj.paginator.num_pages
    context = {
        'service_obj': service_obj,
        'last_page': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'services.html', context=context)

def gallery(request):

    """getting all the gallery images from db"""
    obj = Gallery.objects.all().order_by("-id")
    paginator = Paginator(obj, 8)
    page_number = request.GET.get('page')
    gallery_obj = paginator.get_page(page_number)
    total_pages = gallery_obj.paginator.num_pages

    context = {
        'gallery_obj': gallery_obj,
        'last_page': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, 'gallery.html', context=context)

def contactus(request):

    """gettign address from db"""
    add_obj = Address.objects.last()

    context = {
        'add_obj': add_obj
    }
    try:
        """getting the contact data from contact-us page and saving to db"""
        if request.method == "POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            email = request.POST["email"]
            message = request.POST["msg"]

            contact_obj = Contact(name=name, phone=phone, email=email, message=message)
            contact_obj.save()
            msg = f"""
                Hello Team,\n
                Greetings !!!\n\n
                
                {message}'\n\n
                
                Thanks and Regards,\n
                {name}\n
                Phone : {phone}
            """
            """Receiveing contact message from the Client"""
            receive_email_from_client(name, email, msg)
    except:
        pass

    return render(request, "contact_us.html", context=context)

def team(request):

    obj = Team.objects.all()
    # Paginator logic
    paginator = Paginator(obj, 4)
    page_number = request.GET.get('page')
    team_obj = paginator.get_page(page_number)
    total_pages = team_obj.paginator.num_pages
    # print(total_pages)
    context = {
        'team_obj': team_obj,
        'last_page': total_pages,
        'total_page': [page+1 for page in range(total_pages)]
    }
    return render(request, 'team-detail.html', context=context)

def teamdetailscard(request, pk):
    team_obj = Team.objects.get(pk=pk)

    context = {
        'team_obj': team_obj
    }
    return render(request, 'team-details-card.html', context=context)

def donateus(request):
    """getting the payments methods from db"""
    donate_obj = Donate.objects.last()

    context = {
        'donate_obj': donate_obj
    }
    """saving the donor's detail to db"""
    if request.method == 'POST':
        name = request.POST['name']
        mode = request.POST['pay']
        amt = request.POST['amt']
        trans_id = request.POST['trans']

        pay = Payments(pay_name=name, pay_mode=mode, pay_amount=amt, pay_trans_id=trans_id)
        pay.save()

    return render(request, "donation.html", context=context)

