from django.shortcuts import render

from pizza.models import Pizza


def home(request):
    pizzas = Pizza.objects.order_by('-date_added')[:3]
    return render(request, 'app/index.html', {'pizzas': pizzas})


def contact(request):
    return render(request, 'app/contact.html')
