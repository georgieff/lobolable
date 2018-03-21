from django.urls import path

from .views import home, item

urlpatterns = [
    path('', home, name="pizza_all"),
    path('<pizza_url>/', item, name="pizza_item")
]