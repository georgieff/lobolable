from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=300)
    url_name = models.CharField(max_length=300)
    data_added = models.DateTimeField(auto_now_add=True)


class PizzaComment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.PROTECT)
    data_added = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)

# python manage.py makemigrations
# python manage.py sqlmigrate pizza 0002;2D
# python manage.py migrate