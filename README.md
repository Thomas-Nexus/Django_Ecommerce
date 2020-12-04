# Django_Ecommerce

A 007 themed ecommerce site with add to cart and checkout functionality. This was created in Django with HTML and CSS for front-end development.

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
   

## Permissions

Admin users are given specific permissions and are able to view an order/customer panel summarising all core data. 

The navigation bar is structured to render different options depending on whether the user is logged in/out and if they are an admin/customer.

Two decorators are used for access purposes differentiating between admin and customer groups:

    - unauthenticated_user
    - allowed_users
    

## Product Page Example

![Slide1](https://user-images.githubusercontent.com/72507931/101178819-59111d00-3641-11eb-9b77-f66d05e98fe0.JPG)


## Profile Page Example

![Slide1](https://user-images.githubusercontent.com/72507931/101179560-4d722600-3642-11eb-99ad-9e67bcb004df.JPG)


## Cart Page Example

![Slide1](https://user-images.githubusercontent.com/72507931/101179925-cb363180-3642-11eb-81c0-8b7aa8dcdcb1.JPG)

## Favourites Example

![Slide1](https://user-images.githubusercontent.com/72507931/101180189-28ca7e00-3643-11eb-9e64-28c7379f9e96.JPG)
