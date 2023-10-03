from django.shortcuts import render,redirect
from . forms import UserRegisterForm
from django.contrib.auth.models import User
# Create your views here.

def contactus(request):
    return render(request,'contactus_module/contactus_page.html')

#----------------------------------------------
def user_register(request):
    if request.method=='POST':
        form_register=UserRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password_2']
                                     )
            return redirect('home_module:home')
    else:
        form_register=UserRegisterForm()
    context={'form_register':form_register}
    return render(request,'contactus_module/register.html',context)


