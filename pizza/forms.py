from django.forms import ModelForm

from .models import PizzaComment


class PizzaCommentForm(ModelForm):
    class Meta:
        model = PizzaComment
        exclude = ('user', 'pizza', 'date_added')
