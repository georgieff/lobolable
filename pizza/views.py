from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView, View, DetailView

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from .forms import PizzaCommentForm
from pizza.models import Pizza, PizzaComment


class HomeView(ListView):
    model = Pizza
    template_name = "pizza/index.html"
    context_object_name = 'pizzas'


class ItemView(View):
    template_name = "pizza/item.html"
    initial = {}
    form_class = PizzaCommentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {
            'form': form,
            'pizza': get_object_or_404(Pizza, url_name=self.kwargs['pizza_url'])
        })

    def post(self, request, *args, **kwargs):
        pizza = get_object_or_404(Pizza, url_name=self.kwargs['pizza_url']);
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
                return redirect(pizza)


class PdfView(View):
    template_name = "pizza/pdf.html"

    def get(self, request, *args, **kwargs):
        pizza = get_object_or_404(Pizza, url_name=self.kwargs['pizza_url']);
        pdf_doc = self._render_to_pdf({'pizza': pizza})
        return HttpResponse(pdf_doc, content_type='application/pdf')

    def _render_to_pdf(self, context_dict):
        template = get_template(self.template_name)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

