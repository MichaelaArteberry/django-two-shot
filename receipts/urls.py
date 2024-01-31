from django.urls import path
from receipts.views import create_receipt, ReceiptCreate




urlpatterns = [
    path("", create_receipt, name="home"),
    path("create/", ReceiptCreate, name="create_receipt")
]
