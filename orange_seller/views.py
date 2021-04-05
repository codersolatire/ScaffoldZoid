from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import RequestContext
from decimal import *
from django.core.files.storage import FileSystemStorage

# Create your views here.


def login(request):
    # return HttpResponse("This is Login Page")
    if "user_id" in request.COOKIES.keys():
        return redirect(dashboard)

    if(request.method == "GET"):
        return render(request, "login.html", {})
    elif(request.method == "POST"):
        username = request.POST['username']
        orange_data = ""
        a = Users.objects.filter(username=username)
        if(a.count() != 0):
            if(request.POST['password'] == a[0].password):
                userid = a[0].user_id
                username = a[0].username
                first_name = a[0].user_first_name
                user_type = a[0].user_type

                if(user_type == "Buyer"):
                    orange_data = Oranges.objects.all()

                response = render(request, "dashboard.html",
                                  {'user_type': user_type, 'orange_data': orange_data})
                response.set_cookie("user_id", userid)
                return response
            else:
                # return HttpResponse("Password is wrong")
                return render(request, "login.html", {"message": "Wrong Password"})
        else:
            return render(request, "login.html", {"message": "User does not exist"})


def register(request):
    if(request.method == "GET"):
        return render(request, "signup.html", {})
    elif(request.method == "POST"):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email_id = request.POST['email_id']
        user_type = request.POST['user_type']

        users = Users()
        users.user_first_name = first_name
        users.user_last_name = last_name
        users.username = username
        users.password = password
        users.email_id = email_id
        users.user_type = user_type
        users.save()
        return redirect(login)


def dashboard(request):
    if "user_id" in request.COOKIES.keys():
        orange_data = ""
        user_type = Users.objects.filter(
            user_id=request.COOKIES['user_id'])[0].user_type

        if(user_type == "Buyer"):
            orange_data = Oranges.objects.all()

        return render(request, "dashboard.html", {'user_type': user_type, 'orange_data': orange_data})
    else:
        return redirect(login)
    # return HttpResponse("Dashboard")


def profile(request):
    user_data = Users.objects.filter(user_id=request.COOKIES['user_id'])
    return render(request, "profile.html", {'user_data': user_data[0], 'user_id': request.COOKIES['user_id'], 'user_type': user_data[0].user_type})


def edit_profile(request):
    if(request.method == "POST"):
        user_data = Users.objects.filter(user_id=request.COOKIES['user_id'])
        user_data.update(user_first_name=request.POST.get('first_name'))
        user_data.update(user_last_name=request.POST.get('last_name'))
        user_data.update(username=request.POST.get('username'))
        user_data.update(email_id=request.POST.get('email_id'))

        if(request.FILES):
            myfile = request.FILES['profile_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            import os
            os.system("mkdir static/uploads/"+request.COOKIES['user_id'])
            os.system("mv "+filename+" static/uploads/" +
                      request.COOKIES['user_id']+"/"+filename)

            user_data.update(profile_picture=uploaded_file_url)

        return redirect(profile)
    else:
        return HttpResponse("Edit Profile")


def save_orange(request):
    oranges = Oranges()
    if(request.method == "POST"):
        orange_type = request.POST['orange_type']
        orange_rate = request.POST['orange_rate']
        oranges.orange_type = orange_type
        oranges.rate = orange_rate
        oranges.user_id = request.COOKIES['user_id']
        oranges.save()
        return render(request, "new_orange.html", {})
    elif(request.method == "GET"):
        return render(request, "new_orange.html", {})


def orange_list(request):
    if(request.COOKIES['user_id']):
        user_type = Users.objects.filter(
            user_id=request.COOKIES['user_id'])[0].user_type
        if(request.GET.get('seller_id')):
            orange_data = Oranges.objects.filter(
                user_id=request.GET.get('seller_id'))
            return render(request, "oranges_list.html", {'orange_data': orange_data, 'user_type': user_type})
        if(user_type == "Seller"):
            orange_data = Oranges.objects.filter(
                user_id=request.COOKIES['user_id'])
        elif(user_type == "Buyer"):
            orange_data = Oranges.objects.all()
        return render(request, "oranges_list.html", {'orange_data': orange_data, 'user_type': user_type})
    else:
        return redirect(login)


def seller_list(request):
    if(request.COOKIES['user_id']):
        seller_data = Users.objects.filter(user_type="Seller")
        return render(request, "seller_list.html", {'seller_data': seller_data, 'user_id': request.COOKIES['user_id']})


def update_orange(request):
    if(request.method == "POST"):
        orange_id = request.POST.get('orange_id')
        orange_type = request.POST.get('orange_type')
        orange_rate = request.POST.get('orange_rate')

        orange_data = Oranges.objects.filter(orange_id=orange_id)
        orange_data.update(orange_type=orange_type)
        orange_data.update(rate=orange_rate)
        return redirect(orange_list)
    else:
        return render(request, "404.html", {})


def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('user_id')
    return response
