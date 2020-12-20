from django.contrib import admin
from .models import ExpenseCategory, Expenses

admin.site.register(ExpenseCategory)
admin.site.register(Expenses)
