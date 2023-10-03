from django.contrib import admin
from . import models
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title','email','fullname','created_date']
    list_editable = ['email','fullname']

admin.site.register(models.ContactUs,ContactUsAdmin)