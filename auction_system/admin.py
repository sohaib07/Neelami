from django.contrib import admin

# Register your models here.
from .models import Product,Seller,Bidder
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Bidder)

