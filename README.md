# Rainbow Felt Designs Website

## Overview

### What is this website for?

This is a website for Rainbow Felt Designs to sell homemade crafted products in the UK.

### What does it do?

This website is made to allow users to browse through and purchase crafted products. Users will be able to create an
account, login and add products to a cart which they can then purchase with paypal. Users will be able to request
custom products to be made, view information about all products and business.

### How does it work

This website uses **Django** as a base framework for site and for handling of databases. The site is styled with
**Bootstrap**, mainly used for Nav-Bar, creating columns and making forms with the use of **Django forms bootstrap**. 
Small section of **CSS** code for collapsing navbar is from StackOverflow, see credits section for details.
**Javascript/JQuery** has been used to improve the UX by improving responsiveness through **AJAX**, e.g. resize main
container of site to fit users browser and to allow users to lookup to their postcode to make address input easier.
**Django Carton** has been used to add shopping cart functionality to website, I've altered some of the code to add the
ability to pay for contents of cart with **PayPal**. **PayPal** is used to pay for products using **Django PayPal**,
PayPal is in sandbox mode for testing purposes, some settings would have to be changed for production. This website has
been deployed on **Heroku** to be viewed and tested, you can see the site in action
[HERE](https://rainbow-felt-designs.herokuapp.com)

## Features

### Existing Features
- Eye catching home page with image carousel
- Products page to browse through all available products
- Ability to view separate pages of products to see description and pictures
- Ability to register an account, login and log off
- Page to request custom products
- Ability to add products to cart
- About page describing the store
- Pay for cart contents using **PayPal**
- Ability to lookup address from postcode

### Features Left to Implement
- None

## Tech Used

### Some the tech used includes:
- **HTML**, **CSS**, **Javascript** and **Python**
    - Are base languages for the website
- [Bootstrap](http://getbootstrap.com/)
    - Used to give my project a simple, responsive layout
- [jQuery](https://jquery.com)
	- Need for Bootstrap functionality and most of my javascript code
- [Django](https://www.djangoproject.com)
    - Used as base framework for the site
- [SQLite](https://www.sqlite.org)
    - Using **Django's** inbuilt functionality to create and modify database
- [Django Carton](https://github.com/lazybird/django-carton)
	- Used as a base to create shopping cart for the site
- [Django Forms Bootstrap](https://github.com/pinax/django-forms-bootstrap)
	- Used to create Bootstrap stylized forms with ease in Django
- [Django PayPal](https://github.com/spookylukey/django-paypal)
    - Used to allow **Django** to talk to **PayPal** API
- [Font Awesome](http://fontawesome.io)
	- Used for some of the icons on the site
- [Jasmine](https://jasmine.github.io)
    - Used to test my javascript
- [WhiteNoise](http://whitenoise.evans.io/en/stable/)
    - Used to serve static files once deployed on **Heroku**
- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro)
    - Used to make postcode/address lookup
    
## Testing
- Used built in **Django** testing functionality to test my views and forms for my apps
- Used **Jasmine** to test postcode validation javascript
- Tested functionality and responsiveness of website on various devices/browsers (see below)

### Tested on:
- Computer browsers:
    - Opera, Firefox, Chrome, Edge
- Android phone:
    - Chrome
- iPhone and iPad:
    - Safari

## Contributing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **Python 2.7.14** installed
    - You can get **Python** by installing it from [here](https://www.python.org/downloads/release/python-2714/)
3. Ensure you have **pip** installed by running ```pip --version```, it should be installed from Python installation
4. Install virtualenv with ```pip install virtualenv``` then create a virtual environment with ```virtualenv rainbow```
5. Activate your virtual environment using ```rainbow\scripts\activate```
6. Make sure you are in project root directory and use ```pip install -r requirements\dev.txt``` to install requirements
7. Now you can run the project using ```python manage.py runserver```
8. The project will now run on [localhost](http://127.0.0.1:8000)
9. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits
- A lot of images used were from [Pixabay](https://pixabay.com)
- Some images from [Etsy](https://www.etsy.com/uk/)
- Section of CSS for collapsing navbar menu was by user ZimSystem from [StackOverflow](https://stackoverflow.com/a/36289507)