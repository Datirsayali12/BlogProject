from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from home.forms import ImageForm

from home.models import Image





def blogHome(request):
    messages.success(request, "welcome to BlogHome")
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'blogHome.html', {'form': form, 'img': img})



def blogPost(request,slug):
    post=Image.objects.filter(slug=slug).first()
    return render(request,'blogPost.html',{'post':post})