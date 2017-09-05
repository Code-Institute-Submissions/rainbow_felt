# Imports
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth, messages
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm


# Register function
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        # Check form is valid then save details
        if form.is_valid():
            user = form.save()
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))

            # If details correct then login
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered your account.")
                return redirect(reverse('myaccount'))

            # If details incorrect show error msg
            else:
                messages.error(request, "We have been unable to register you at this time.")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

            if user:
                auth.login(request, user)
                messages.error(request, "You have logged in successfully.")
                return redirect(reverse('myaccount'))
            else:
                form.add_error(None, 'Your email and/or password was not recognised')

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def myaccount(request):
    return render(request, 'myaccount.html')
