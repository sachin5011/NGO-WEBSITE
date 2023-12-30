from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator

def blog(request):
    """getting blog details from db"""
    obj = Blog.objects.all()
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    total_pages = blog_obj.paginator.num_pages

    context = {
        'blog_obj': blog_obj,
        'last_page': total_pages,
        'total_page': [page + 1 for page in range(total_pages)]
    }
    return render(request, "blog.html", context=context)

def blog_details(request, pk):
    blog_obj = Blog.objects.get(pk=pk)

    context={
        'blog_obj': blog_obj
    }
    return render(request, 'blog-post-details.html', context=context)
