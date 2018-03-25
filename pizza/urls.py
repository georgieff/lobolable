from django.urls import path

from .views import HomeView, PdfView, ItemView

urlpatterns = [
    path('', HomeView.as_view(), name="pizza_all"),
    path('<pizza_url>/', ItemView.as_view(), name="pizza_item"),
    path('pdf/<pizza_url>/', PdfView.as_view(), name="pizza_pdf")
]