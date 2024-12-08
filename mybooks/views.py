from django.shortcuts import render,redirect

from .forms import SingUpForm

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm



#Create your views here.


def signup_view(request):

    if request.method == "POST":

        form = SingUpForm(request.POST)

        if form.is_valid():

            form.save()  # Save the new user

            return redirect('login')  # Redirect to login page after successful signup
        
    else:

        form = SingUpForm()

    return render(request, 'signup.html', {'form': form})






def signin_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect('home')  # Redirect to home or dashboard after successful login
            
            else:

                form.add_error(None, "Invalid username or password")

    else:

        form = AuthenticationForm()

    return render(request, 'myapp/signin.html', {'form': form})

