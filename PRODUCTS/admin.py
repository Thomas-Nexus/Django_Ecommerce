from django.contrib import admin
from .models import *

admin.site.register(PRODUCTS)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(CartItem)
admin.site.register(Favourite)
admin.site.register(Shipping)
admin.site.register(Payment)


