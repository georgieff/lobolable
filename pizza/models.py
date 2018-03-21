from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='pizzas', blank=True)
    ingredients = models.TextField(max_length=3000, blank=True)
    preparation = models.TextField(max_length=3000, blank=True)
    url_name = models.CharField(max_length=300, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PizzaComment(models.Model):
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField(max_length=3000)

    def __str__(self):
        return "for \"{0}\" by {1}".format(self.pizza.name, self.user)

# python manage.py makemigrations
# python manage.py sqlmigrate pizza
# python manage.py migrate