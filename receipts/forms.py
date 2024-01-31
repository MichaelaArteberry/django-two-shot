from django import forms
from django.db import models
from receipts.models import Receipt
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
