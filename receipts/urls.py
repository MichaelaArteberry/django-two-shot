from django.urls import path
from receipts.views import create_receipt, ReceiptCreate, category_list, account_list, CreateExpense, CreateAccount




urlpatterns = [
    path("", create_receipt, name="home"),
    path("create/", ReceiptCreate, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list" ),
    path("categories/create/", CreateExpense, name="create_category"),
    path("accounts/create/", CreateAccount, name="create_account"),
]
