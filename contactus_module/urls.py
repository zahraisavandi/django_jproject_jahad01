from django.urls import path
from . import views
app_name='contactus_module'
urlpatterns=[
    path('',views.contactus,name='contact-us'),
    path('register/',views.user_register,name='user-register')
]


