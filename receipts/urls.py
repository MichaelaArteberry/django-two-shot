from django.urls import path
from receipts.views import create_receipt, ReceiptCreate, category_list, account_list




urlpatterns = [
    path("", create_receipt, name="home"),
    path("create/", ReceiptCreate, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list" ),
]
