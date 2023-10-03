from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

#------------class ProductCategory...one to many
class ProductCategory(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    url_title=models.CharField(max_length=300,verbose_name='عنوان در url')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'

#---------------ProductInformation...one to one
class ProductInformation(models.Model):
    color=models.CharField(max_length=300,verbose_name='رنگ')
    size=models.CharField(max_length=300,verbose_name='سایز')

    def __str__(self):
        return f'{self.color}-----{self.size}'

    class Meta:
        verbose_name='اطلاعات تکمیلی'
        verbose_name_plural='لیست اطلاعات تکمیلی'

#-----------------ProductTag....many to many
class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='عنوان تگ')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='تگ های محصولات'

#---------------Product
class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')
    product_information=models.OneToOneField(ProductInformation,on_delete=models.CASCADE,null=True,
                                             blank=True,related_name='product_info',verbose_name='اطلاعات تکمیلی')
    product_tag=models.ManyToManyField(ProductTag,verbose_name='تگ محصول')
    title=models.CharField(max_length=100,verbose_name='عنوان محصول')
    price=models.IntegerField(verbose_name='قیمت محصول')
    description=models.CharField(max_length=300,verbose_name='توضیحات محصول')
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال بودن محصول')
    ratings=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)],verbose_name='امتیاز محصول')
    slug = models.SlugField(max_length=400,unique=True,default='', null=False, db_index=True, verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}-----{self.price}'

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'

    def get_absolute_url(self):
        return reverse('product-details', args=[self.slug])

