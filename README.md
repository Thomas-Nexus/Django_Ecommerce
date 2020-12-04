# Django_Ecommerce

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
   

<b>Permissions </b>

Admin users are given specific permissions and are able to view an order/customer panel summarising all core data. 

The navigation bar is structured to render different options depending on whether the user is logged in/out and if they are an admin/customer.

Two decorators are used for access purposes differentiating between admin and customer groups:

    - unauthenticated_user
    - allowed_users


## Screenshot Example (Film Page)
    
![Spectre](https://user-images.githubusercontent.com/72507931/99554599-49de6e00-29b7-11eb-9681-7922c27d3a91.JPG)
