from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import CreateForm

# Create your views here.

@login_required
def create_receipt(request):
  model_list = Receipt.objects.filter(purchaser=request.user)
  context = {
    "receipt_list": model_list
  }
  return render(request, "receipts/receipts.html", context)




@login_required
def ReceiptCreate(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateForm()
        context = {
            "form": form,
        }
        return render(request, "receipts/create.html", context)






@login_required
def category_list(request):
    things = ExpenseCategory.objects.filter(owner=request.user)
    context = {
    "category_list": things
    }
    return render(request, "receipts/expense_category.html", context)






@login_required
def account_list(request):
    things = Account.objects.filter(owner=request.user)
    context = {
    "account_list": things
    }
    return render(request, "receipts/account_list.html", context)
