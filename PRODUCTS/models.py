from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
#-----------------------------------------------------------------------------------------------------------------------

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name

# -----------------------------------------------------------------------------------------------------------------------

class PRODUCTS(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("PRODUCTS/product", kwargs={"pk": self.pk})

    def get_add_to_cart_url(self):
        return reverse("PRODUCTS/add_to_cart", kwargs={"pk": self.pk})

    def get_remove_from_cart_url(self):
        return reverse("PRODUCTS/remove_from_cart", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------------------------------------

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(PRODUCTS, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        Cart = CartItem.objects.all()
        total = sum([item.get_total_item_price for item in Cart])
        string = str(total)
        return string

    def unique_films(self):
        Cart = CartItem.objects.all()
        for x in Cart:
            return f'{x.quantity}'

    @property
    def get_total_item_price(self):
        return self.quantity * self.product.price

#-----------------------------------------------------------------------------------------------------------------------

class Shipping(models.Model):
    account = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    fullname = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

#-----------------------------------------------------------------------------------------------------------------------

class Payment(models.Model):
    name_on_card = models.CharField(max_length=40, null=True)
    card_number = models.CharField(max_length=16, null=True)
    expiry = models.CharField(max_length=4, null=True)
    security_code = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.card_number

#-----------------------------------------------------------------------------------------------------------------------

class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)
    total = models.CharField(max_length=200, null=True)
    items = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    STATUS = (('PAID', 'PAID'), ('IN CART', 'IN CART'))
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.user.username

#-----------------------------------------------------------------------------------------------------------------------

BOND = (('Sean Connery', 'Sean Connery'), ('George Lazenby', 'George Lazenby'), ('Roger Moore', 'Roger Moore'),
       ('Timothy Dalton', 'Timothy Dalton'), ('Pierce Brosnan', 'Pierce Brosnan'), ('Daniel Craig', 'Daniel Craig'))

FILMS = (
    ('DR.NO', 'DR.NO'), ('FROM RUSSIA WITH LOVE', 'FROM RUSSIA WITH LOVE'), ('GOLDFINGER', 'GOLDFINGER'),
    ('THUNDERBALL', 'THUNDERBALL'), ('YOU ONLY LIVE TWICE', 'YOU ONLY LIVE TWICE'),
    ('ON HER MAJESTYS SECRET SERVICE', 'ON HER MAJESTYS SECRET SERVICE'),
    ('DIAMONDS ARE FOREVER', 'DIAMONDS ARE FOREVER'), ('LIVE AND LET DIE', 'LIVE AND LET DIE'),
    ('THE MAN WITH THE GOLDEN GUN', 'THE MAN WITH THE GOLDEN GUN'), ('THE SPY WHO LOVED ME', 'THE SPY WHO LOVED ME'),
    ('MOONRAKER', 'MOONRAKER'), ('FOR YOUR EYES ONLY', 'FOR YOUR EYES ONLY'), ('OCTOPUSSY', 'OCTOPUSSY'),
    ('A VIEW TO A KILL', 'A VIEW TO A KILL'), ('THE LIVING DAYLIGHTS', 'THE LIVING DAYLIGHTS'),
    ('LICENCE TO KILL', 'LICENCE TO KILL'), ('GOLDENEYE', 'GOLDENEYE'), ('TOMORROW NEVER DIES', 'TOMORROW NEVER DIES'),
    ('THE WORLD IS NOT ENOUGH', 'THE WORLD IS NOT ENOUGH'), ('DIE ANOTHER DAY', 'DIE ANOTHER DAY'),
    ('CASINO ROYALE', 'CASINO ROYALE'), ('QUANTUM OF SOLACE', 'QUANTUM OF SOLACE'), ('SKYFALL', 'SKYFALL'),
    ('SPECTRE', 'SPECTRE'), ('NO TIME TO DIE', 'NO TIME TO DIE'),
)

class Favourite(models.Model):
     bond = models.CharField(max_length=100, choices=BOND, default='Favourite Bond')
     film = models.CharField(max_length=100, choices=FILMS, default='Favourite Film')

     def __str__(self):
         return f'{self.bond} | {self.film}'