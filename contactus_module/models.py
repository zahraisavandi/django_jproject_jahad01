from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    email=models.EmailField(max_length=300,verbose_name='ایمیل')
    fullname=models.CharField(max_length=300,verbose_name='نام و نام خانوداگی')
    message=models.TextField(verbose_name='متن پیام')
    created_date=models.DateTimeField(verbose_name='تاریخ ایجاد',auto_now_add=True)
    response=models.TextField(verbose_name='متن پاسخ', blank=True,null=True)
    is_read_by_admin=models.BooleanField(verbose_name='خوانده شده توسط ادمین',default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='لیست تماس با ما'