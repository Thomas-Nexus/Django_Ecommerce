from .forms import *
from .models import *
from django.utils import timezone
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
# -----------------------------------------------------------------------------------------------------------------------

def home_view(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def actors(request):
    return render(request, 'actors.html')

def notimetodie(request):
    return render(request, 'notimetodie.html')

def spectre(request):
    return render(request, 'spectre.html')

def skyfall(request):
    return render(request, 'skyfall.html')

def quantumofsolace(request):
    return render(request, 'quantumofsolace.html')

def casinoroyale(request):
    return render(request, 'casinoroyale.html')

#-----------------------------------------------------------------------------------------------------------------------

def nav(request):
    cart = CartItem.objects.all()
    context = {count: 'count'}
    return render(request, 'navbar.html', context)

#-----------------------------------------------------------------------------------------------------------------------

def favourites(request):
    form = FavouriteForm()
    if request.method == 'POST':
        form = FavouriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/favourites')
    context = {'form': form}
    return render(request, 'favourites.html', context)

#-----------------------------------------------------------------------------------------------------------------------

class ProductView(DetailView):
    model = PRODUCTS
    template_name = "PRODUCTS/detail.html"


class OrderSummary(View):
    def get(self, *args, **kwargs):
        try:
            order = Orders.objects.get(user=self.request.user)
            cart = CartItem.objects.all
            product = PRODUCTS.objects.all
            total = CartItem

            context = {'object': order, 'cart': cart, 'product': product, 'total': total}
            return render(self.request, 'PRODUCTS/cart.html', context)

        except ObjectDoesNotExist:
            Orders.objects.create(user=self.request.user)
            return redirect("PRODUCTS:order-summary")

#-----------------------------------------------------------------------------------------------------------------------

def add_to_cart(request, pk):
    product = get_object_or_404(PRODUCTS, pk=pk)

    try:
        order_item = CartItem.objects.get(product=product, user=request.user)
        order_qs = Orders.objects.filter(user=request.user, complete=False)
        if order_qs.exists():
            order = order_qs[0]
            if order_item:
                order_item.quantity += 1
                order_item.save()
                return redirect("PRODUCTS:order-summary")
        else:
            ordered_date = timezone.now()
            order = Orders.objects.create(user=request.user, date=ordered_date)
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "ADDED TO CART")
            return redirect('PRODUCTS:order-summary')
    except:
        CartItem.objects.create(product=product, user=request.user)
        return redirect('PRODUCTS:order-summary')

#-----------------------------------------------------------------------------------------------------------------------

def reduce_quantity_item(request, pk):
    product = get_object_or_404(PRODUCTS, pk=pk)
    order_qs = Orders.objects.filter(user=request.user, complete=False)
    order_item = CartItem.objects.filter(product=product, user=request.user, ordered=False)[0]
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    messages.info(request, 'Quantity Updated')
    return redirect("PRODUCTS:order-summary")

#-----------------------------------------------------------------------------------------------------------------------

def remove_from_cart(request, pk):
    product = get_object_or_404(PRODUCTS, pk=pk)
    order_qs = Orders.objects.filter(user=request.user, complete=False)

    if order_qs.exists():
        order = order_qs[0]
        order_item = CartItem.objects.filter(product=product, user=request.user, ordered=False)[0]
        order_item.delete()
        messages.info(request, 'Item Removed From Cart')
        return redirect('PRODUCTS:order-summary')

#-----------------------------------------------------------------------------------------------------------------------

def confirm(request):
    cart = CartItem.objects.all()
    total = CartItem
    context = {'cart': cart, 'total': total}
    return render(request, 'PRODUCTS/confirm.html', context)

#-----------------------------------------------------------------------------------------------------------------------

def final(request):
    cart = CartItem.objects.all()
    order = Orders.objects.get(user=request.user)
    order.complete = True
    order.status = 'PAID'

    transaction = CartItem()
    order.total = f'{transaction}'

    film_count = CartItem()
    film_count2 = film_count.unique_films()
    order.items = f'{film_count2}'
    order.shipping = Shipping.objects.get(user=request.user)

    order.save()
    cart.delete()
    return redirect('/confirmation')

#-----------------------------------------------------------------------------------------------------------------------

def confirmation(request):
    return render(request, 'PRODUCTS/confirmation.html')

#-----------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
@allowed_users(allowed=['Admin'])
def panel(request):
    order = Orders.objects.all()
    total = Orders.total
    customers = Customer.objects.all()
    total_orders = order.count()
    total_customers = customers.count()
    paid = order.filter(status='PAID').count()

    context = {'order': order, 'customers': customers, 'total_orders': total_orders,
               'total_customers': total_customers, 'paid': paid, 'total': total}
    return render(request, 'PRODUCTS/panel.html', context)

# -----------------------------------------------------------------------------------------------------------------------

def checkout(request):
    items = CartItem.objects.all()
    form = ShippingForm()
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/payment')
    total = CartItem

    context = {'items': items, 'form': form, 'total': total}
    return render(request, 'PRODUCTS/checkout.html', context)

#-----------------------------------------------------------------------------------------------------------------------

def payment(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/confirm')
    context = {'form': form}
    return render(request, 'PRODUCTS/payment.html', context)

# -----------------------------------------------------------------------------------------------------------------------

def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            messages.success(request, 'Account successfully created for ' + username)
            return redirect('/login')

    context = {'form': form}
    return render(request, 'PRODUCTS/register.html', context)

# -----------------------------------------------------------------------------------------------------------------------

def login_p(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username Or Password Incorrect')
    context = {}
    return render(request, 'PRODUCTS/login.html', context)

def logout_p(request):
    logout(request)
    return redirect('/login')

# -----------------------------------------------------------------------------------------------------------------------

def profile(request):
    customer = request.user.customer
    form = ProfileForm(instance=customer)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/profile')

    context = {'form': form}
    return render(request, 'PRODUCTS/profile.html', context)
