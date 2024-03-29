from django import forms
from django.db import models
from receipts.models import Receipt, ExpenseCategory, Account
from django.forms import ModelForm


class CreateForm(ModelForm):
    class Meta:
        model = Receipt
        fields = (
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        )



class ExpenseForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = (
            "name",
        )



class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "name",
            "number",
        )
