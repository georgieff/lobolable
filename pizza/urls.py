from django.urls import path

from .views import HomeView, item, pdf

urlpatterns = [
    path('', HomeView.as_view(), name="pizza_all"),
    path('<pizza_url>/', item, name="pizza_item"),
    path('pdf/<pizza_url>/', pdf, name="pizza_pdf")
]