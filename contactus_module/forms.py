from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    password_1=forms.CharField(max_length=50)
    password_2=forms.CharField(max_length=50)

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد')
        return email

    def clean_password_2(self):
        password1=self.cleaned_data['password_1']
        password2=self.cleaned_data['password_2']
        if password1!=password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('password was short')
        elif not any (i.isupper() for i in password2):
            raise forms.ValidationError('حداقف باید یک حرف بزرگ داشته باشد')
        return password1

#-----------------
class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()


