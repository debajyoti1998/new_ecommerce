from django.contrib import admin
from .models import Costomar,Product,Cart,OrderPlaced
# Register your models here.

@admin.register(Costomar)
class CostomarAdmin(admin.ModelAdmin):
    list_display=['name','location','city','zipcode','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','selling_price','discount_price','description','brand','catagory','product_image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['user','Product','quality']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['user','customar','Product','quantity','ordered_date','status']
