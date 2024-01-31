from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_receipt(request):
  model_list = Receipt.objects.filter(purchaser=request.user)
  context = {
    "receipt_list": model_list
  }
  return render(request, "receipts/receipts.html", context)
