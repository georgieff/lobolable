from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import PizzaCommentForm
from pizza.models import Pizza, PizzaComment


def home(request):

    return render(request, 'pizza/index.html',
                  {
                      'pizzas': Pizza.objects.order_by('-date_added')
                  })


def item(request, pizza_url):
    pizza = get_object_or_404(Pizza, url_name=pizza_url)

    if request.method == "POST":
        return _add_comment(request, pizza)
    else:
        form = PizzaCommentForm()

    return render(request, 'pizza/item.html',
                  {
                      'pizza': pizza,
                      'comments': PizzaComment.objects.order_by('-date_added').filter(pizza=pizza),
                      'form': form
                  })


def pdf(request, pizza_url):
    pizza = get_object_or_404(Pizza, url_name=pizza_url)
    pdf_doc = _render_to_pdf('pizza/pdf.html', {'pizza': pizza})

    return HttpResponse(pdf_doc, content_type='application/pdf')


def _add_comment(request, pizza):
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


def _render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
