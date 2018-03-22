from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import  PizzaCommentForm
from pizza.models import Pizza, PizzaComment


def home(request):

    return render(request, 'pizza/index.html',
                  {
                      'pizzas': Pizza.objects.order_by('-date_added')
                  })


def item(request, pizza_url):
    pizza = get_object_or_404(Pizza, url_name=pizza_url)

    if request.method == "POST":
        return add_comment(request, pizza)
    else:
        form = PizzaCommentForm()

    return render(request, 'pizza/item.html',
                  {
                      'pizza': pizza,
                      'comments': PizzaComment.objects.order_by('-date_added').filter(pizza=pizza),
                      'form': form
                  })


def add_comment(request, pizza):
    pizza_comment = PizzaComment(user=request.user, pizza=pizza)
    form = PizzaCommentForm(instance=pizza_comment, data=request.POST)

    if form.is_valid():
        form.save()
        comments = PizzaComment.objects.order_by('-date_added').filter(pizza=pizza)
        if request.is_ajax():
            rendered_comments = render_to_string('partials/comments.html', {
                'comments': comments
            })
            return JsonResponse({'comments': rendered_comments})
        else:
            return redirect('pizza_item', pizza_url=pizza.url_name)