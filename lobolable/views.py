from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')


def contact(request):
    return render(request, 'app/contact.html')
