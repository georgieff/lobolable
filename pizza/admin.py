from django.contrib import admin
from .models import Pizza, PizzaComment


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_name', 'date_added')


admin.site.register(PizzaComment)

# @admin.register(PizzaComment)
# class PizzaCommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'pizza.name', 'date_added')