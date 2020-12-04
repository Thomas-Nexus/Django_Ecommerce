from PAGES.views import *
from PRODUCTS.views import *
from django.urls import reverse
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path, register_converter
#-----------------------------------------------------------------------------------------------------------------------
app_name = 'PRODUCTS'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('actors/', actors, name='actors'),
    path('shop/', shop, name='shop'),
    path('favourites/', favourites, name='favourites'),
    path('spectre/', spectre, name='spectre'),
    path('skyfall/', skyfall, name='skyfall'),
    path('notimetodie/', notimetodie, name='notimetodie'),
    path('quantumofsolace/', quantumofsolace, name='quantum'),
    path('casinoroyale/', casinoroyale, name='casino'),
    path('panel/', panel, name='panel'),
    path('profile/', profile, name='profile'),
    path('login/', login_p, name='login'),
    path('logout/', logout_p, name='logout'),
    path('register/', register, name='register'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('confirm/', confirm, name='confirm'),
    path('final/', final, name='final'),
    path('confirmation/', confirmation, name='confirmation'),
    path('cart/', OrderSummary.as_view(), name='order-summary'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('reduce_quantity_item/<int:pk>/', reduce_quantity_item, name='reduce_quantity_item'),
    #path('products/<int:pk>/', ProductView.as_view(), name='product'), #Not used. Can toggle between manual/pk product pages.

    ]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
