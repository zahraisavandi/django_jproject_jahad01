from django.urls import path

from . import views
app_name='product_module'
urlpatterns=[
    path('',views.product_list,name='product-list'),
    # path('<int:product_id>',views.product_detail)
    path('<slug:slug>', views.product_detail,name='product-details'),
]
