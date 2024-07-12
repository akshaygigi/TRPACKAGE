from django.shortcuts import render,redirect
from.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from .models import TourPackage

# Create your views here.
def IndexView(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/loginss')
    else:
        form=Signupform()
    return render(request,'register.html',{'form': form})

def loginss(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(request,username=username,password=password)

            if user:
               login(request, user)
               return redirect('home')
        else:
            form=Loginform()
            return render(request,'login.html',{'form': form})

def package_list(request):
    packages = TourPackage.objects.all()
    return render(request, 'packages.html', {'packages': packages})

def payments(request):
    return render(request,'booking.html')