from django.shortcuts import render, redirect, get_object_or_404

from .forms import  PizzaCommentForm
from pizza.models import Pizza, PizzaComment


def home(request):

    return render(request, "pizza/index.html",
                  {
                      'pizzas': Pizza.objects.order_by('-date_added')
                  })


def item(request, pizza_url):
    pizza = get_object_or_404(Pizza, url_name=pizza_url)

    if request.method == "POST":
        pizza_comment = PizzaComment(user=request.user, pizza=pizza)
        form = PizzaCommentForm(instance=pizza_comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizza_item', pizza_url=pizza_url)
    else:
        form = PizzaCommentForm()

    return render(request, "pizza/item.html",
                  {
                      'pizza': pizza,
                      'comments': PizzaComment.objects.order_by('-date_added').filter(pizza=pizza),
                      'form': form
                  })