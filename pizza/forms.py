from django.forms import ModelForm
from django import forms

from .models import PizzaComment


class PizzaCommentForm(ModelForm):
    comment = forms.CharField(widget=forms.Textarea, label='Your comment')

    class Meta:
        model = PizzaComment
        exclude = ('user', 'pizza', 'date_added')
