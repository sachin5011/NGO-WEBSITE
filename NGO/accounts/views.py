from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def admin_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            return HttpResponseRedirect(request.META.get('HTTP_REFER'))

        user_obj = authenticate(username=username, password=password)

        if user_obj and user_obj.is_superuser:
            login(request, user_obj)
            return redirect('dashboard')
        return redirect('login')

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def add_more_users(request):

    if request.method == 'POST':
        username = request.POST['user']
        new_pass = request.POST['new-pass']
        rpt_pass = request.POST['rpt-pass']
        checked = request.POST.get('check-per', False)
        staff = request.POST.get('check-per', False)
        checked = True if checked else False
        staff = True if checked else False


        if username and new_pass and rpt_pass:
            user_obj = User.objects.filter(username=username)
            if user_obj:
                return redirect('adduser')

            user = User(username=username, password=new_pass, is_superuser=checked, is_staff=staff)

            user.set_password(new_pass)
            user.save()
            return redirect('allusers')

    return render(request, 'accounts/add-user.html')
