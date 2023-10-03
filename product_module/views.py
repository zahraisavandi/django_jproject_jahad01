from django.db.models import Avg,Max,Min
from django.shortcuts import render, get_object_or_404
from . models import Product
# Create your views here.

# def product_list(request):
#     all_product=Product.objects.all()
#     return render(request,'product_module/product_list.html',{'all_product':all_product})

# def product_list(request):
#     all_product=Product.objects.all().order_by('-price')
#     number_of_products=all_product.count()
#     return render(request,'product_module/product_list.html',{'all_product':all_product,'number_of_product':number_of_products})


# # def product_list(request):
# #     all_product=Product.objects.all().order_by('-price')
# #     number_of_products=all_product.count()
# #     info=all_product.aggregate(Avg('price'),Max('price'),Min('price'))
# #     return render(request,'product_module/product_list.html',{'all_product':all_product,
#                                                               'number_of_product':number_of_products,'info':info})

def product_list(request):
    all_product=Product.objects.all().order_by('-price')
    number_of_products=all_product.count()
    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))
    return render(request,'product_module/product_list.html',{'all_product':all_product,
                                                              'number_of_product':number_of_products,
                                                              'info':info})

def product_detail(request,slug):
    products=get_object_or_404(Product,slug=slug)
    return render(request,'product_module/product_details.html',{'product':products})
