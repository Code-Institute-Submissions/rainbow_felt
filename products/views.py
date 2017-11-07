# Imports
from django.shortcuts import render, get_object_or_404
from .models import Product, Custom
from .forms import CustomProductForm
from django.contrib import auth, messages
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse


# View all products in one page
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# View each product individually
def product_view(request, id):
    viewed_product = get_object_or_404(Product, pk=id)
    return render(request, 'productdetails.html', {'viewed_product': viewed_product})


def custom_request(request):
	if request.method == "POST":
		form = CustomProductForm(request.POST)
        # Check form is valid then save details
		if form.is_valid():
			custom = form.save()
			custom = auth.authenticate(email=request.POST.get('email'), custom_description=request.POST.get('custom_description'))

	        # If submitted correctly then show successful msg
			if custom:
				auth.login(request, user)
				messages.success(request, "You have successfully submitted your request.")
				return redirect(reverse('myaccount'))

	        # If details incorrect show error msg
			else:
				messages.error(request, "We have been unable to submit your request at this time.")

	else:
		form = CustomProductForm()

	args = {'form': form}
	args.update(csrf(request))
	return render(request, 'customorder.html', args)
