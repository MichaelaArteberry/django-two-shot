from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.


@admin.register(ExpenseCategory)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]



@admin.register(Account)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "number",
    ]



@admin.register(Receipt)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "vendor",
        "total",
        "tax",
        "date",
    ]
