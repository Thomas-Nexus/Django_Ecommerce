from django.contrib import admin
from django.urls import path, include
#-----------------------------------------------------------------------------------------------------------------------

urlpatterns = [
    path('', include('PRODUCTS.urls', namespace='PRODUCTS')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
