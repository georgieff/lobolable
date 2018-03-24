from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View

from pizza.models import Pizza
from .forms import SignUpForm


class HomeView(ListView):
    queryset = Pizza.objects.order_by('-date_added')[:3]
    template_name = "app/index.html"
    context_object_name = 'pizzas'


class ContactView(TemplateView):
    template_name = "app/contact.html"


class SignUpView(View):
    template_name = 'app/signup.html'
    initial = {}
    form_class = SignUpForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('lobolable_homepage')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


class NotFoundView(TemplateView):
    template_name = "app/404.html"
