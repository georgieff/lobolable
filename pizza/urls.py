from django.urls import path

from .views import home, item, pdf

urlpatterns = [
    path('', home, name="pizza_all"),
    path('<pizza_url>/', item, name="pizza_item"),
    path('pdf/<pizza_url>/', pdf, name="pizza_pdf")
]