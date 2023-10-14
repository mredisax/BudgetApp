from django.contrib import admin
from budgets.models import Budget
from transactions.models import Transaction
# Register your models here.

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0

class BudgetAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ('name',)

    
admin.site.register(Budget, BudgetAdmin)