import io
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Contact,Image
from .forms import ImageForm, PostForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import ImageSerializer,ContactSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.

def home(request):
    messages.success(request, "welcome to Blog")
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'home.html', {'form': form, 'img': img})


def contact(request):
    messages.success(request, "welcome to contact")
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')

        if len(name) < 5 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "form submitted sucessfully!!")
    return render(request, "contact.html")


def about(request):
    messages.success(request, "welcome to about")
    return render(request,'about.html')

def addPost(request):
    messages.success(request, "welcome to addpost")
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'addpost.html', {'form': form, 'img': img})

def search(request):
    if request.method=='GET':
        q=request.GET.get('query')
        img=Image.objects.filter(text__icontains=q)
        return render(request,"search.html",{'img':img})
    else:
        print("no info to show")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        else:
            try:

                myuser = User.objects.create_user(username, email, password1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                messages.success(request, "Your account has been created")
                return redirect('home')
            except IntegrityError as e:

                if 'unique constraint' in str(e):
                    messages.error(request, "Username or email already exists")
                else:
                    messages.error(request, "An error occurred while creating your account")
    else:
        messages.error(request, "Failed to create account")

    return render(request, 'signup.html')


def handleLogin(request):
    if request.method== "POST":
        loginusername=request.POST['username1']
        loginpass1=request.POST['password']
        user=authenticate(username=loginusername,password=loginpass1)
        if user is not None:
            login(request,user)
            messages.success(request,"sucessfully loged in")
            return render(request,"addPost.html")

        else:
            messages.error(request,"Invalid credentails")
            return render(request,"blogHome.html")
    return render(request,"Login.html")

def Logout(request):
    logout(request)
    messages.success(request, "logout sucessfully")
    return redirect("home")

def profile(request,user_name):
    user_related_data=Image.objects.filter(name=user_name)

    return render(request,"profile.html",{'user_related_data':user_related_data})

def Image_list(request):
    stu=Image.objects.all()
    serializer=ImageSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


@api_view(['GET', 'POST'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all().values('username', 'first_name', 'last_name', 'email')
        return Response(data=users, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        username = request.data.get('username')
        fname = request.data.get('first_name')
        lname = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')  

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        return Response({'msg': 'Data created'}, status=status.HTTP_201_CREATED)


@csrf_exempt
def contact_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ContactSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data inserted'}
            #json_data = JSONRenderer.render(res)
            return HttpResponse(json_data, content_type="application/json")
        return HttpResponse(JSONRenderer.render(serializer.errors), content_type="application/json")
