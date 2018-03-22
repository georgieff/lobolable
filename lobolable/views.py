from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from pizza.models import Pizza


def home(request):
    pizzas = Pizza.objects.order_by('-date_added')[:3]
    return render(request, 'app/index.html', {'pizzas': pizzas})


def contact(request):
    return render(request, 'app/contact.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next = request.GET.get('next', '/')
            return redirect(next)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})