from django.urls import path
from receipts.views import create_receipt




urlpatterns = [
    path("", create_receipt, name="home"),
]
