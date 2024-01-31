from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from receipts.models import Receipt

# Create your views here.

def create_receipt(request):
  model_list = Receipt.objects.all()
  context = {
    "receipt_list": model_list
  }
  return render(request, "receipts/receipts.html", context)
