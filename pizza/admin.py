from django.contrib import admin
from pizza.models import Pizza, PizzaComment


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_name', 'data_added')


admin.site.register(PizzaComment)
