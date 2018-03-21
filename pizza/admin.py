from django.contrib import admin

from pizza.models import Pizza, PizzaComment

admin.site.register(Pizza)
admin.site.register(PizzaComment)
