# Django_Full_Ecommerce_Store

A 007 themed ecommerce site with full add to cart and checkout functionality. This is being created in Django with HTML and CSS front-end development.

## Technologies

<b>Languages:</b> 
              
   - Django 3.1.3 (Python 3.8.3) 
   - HTML5
   - CSS

<b>Editor:</b> 
    
   - PyCharm/Command
   - Command Line 

## User Features

Customers are able to complete the following actions:

   - Register an account
   - Amend profile details (name, email, profile picture etc).
   - Login
   - Logout
   - Browse films/actors
   - Submit favourite film/actor
   - Watch trailers for films
   - Add any films to a cart
   - Amend the quantity of items
   - Delete cart items
   - Checkout with the aformentioned items via completion of address and payment forms.
   
Admin users are given specific permissions and are able to view an order/customer panel summarising all inputted data. 

Admin users are not permitted to access the shopping cart.

  
   

## Products Application: Folder Structure Skeleton Map

<b>URL's (Main Project Folder)</b>

    Dynamic:
    - createorder
    - updateorder
    - deleteorder
    - customer
    - products
 
    Static:
    - home
    - admin
    - shop
    - orders
    - profile
    - login
    - logout
    - register
    - cart
    - checkout
    - actors
    - films
    - casinoroyale
    - quantumofsolace
    - skyfall
    - spectre
    - notimetodie


<b>Models</b>

    - Customer (user, name, phone, email, date, profile image)
    - Tag (name)
    - Products (title, description, price, summary, image, tags)
    - Orders (customer, product, date, complete, status)
    - CartItem (product, order, quantity, date added)
    - Shipping (customer, order, address, city, postcode, country, date added)

<b>Views</b>

    - homeview             
    - films
    - actors
    - casinoroyale
    - quantumofsolace
    - skyfall
    - spectre
    - notimetodie
    - orders
    - customer
    - products
    - product detail view
    - cart
    - checkout
    - register
    - login_p
    - logout_p
    - createorder
    - updateorder
    - deleteorder
    - product_form

<b>Forms</b>

    - RegisterUserForm
    - ProfileForm
    - OrdersForm

<b>Admin</b>

Registering all 6 models.


<b>Decorators</b>

Two decorators are used for access purposes differentiating between admin and customer groups:

    - unauthenticated_user
    - allowed_users

A static folder is also used (including sub dirs of css, images and profile images) and implemented into settings.

## Templates (HTML): Folder Structure Summary

All HTML files that are used in conjunction with the views.py will be included below (also will be attached to the repository):

    - home
    - cart
    - checkout
    - createorder (admin only)
    - deleteorder (admin only)
    - customers (admin only)
    - orders (admin only)
    - detail
    - login
    - logout
    - products_shop
    - register
    
    - actors
    - films
    - inheritance
    - navbar
    - casinoroyale
    - quantumofsolace
    - skyfall
    - spectre
    - notimetodie
    
## Screenshot Example (Film Page)
    
![Spectre](https://user-images.githubusercontent.com/72507931/99554599-49de6e00-29b7-11eb-9681-7922c27d3a91.JPG)

## Status

