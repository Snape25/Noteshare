from django.shortcuts import render,redirect
from .models import Categories
from django.views.generic.edit import CreateView
from .models import Categories
from .forms import Registration
from django.contrib.auth import  login
from django.contrib import  messages
# Create your views here.


def index(request):
    categories = Categories.objects.all()
    return  render(request,"baseapp/homepage.html",{'categories':categories})


class createcat(CreateView):
    model = Categories
    fields = ['title']
    template_name= "baseapp/createctg.html"
    success_url = '/'

def register_request(request):
    if request.method=='POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Succesfully registered")
            return redirect("/")
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = Registration
    return render(request=request, template_name="baseapp/register.html", context={"register_form": form})


