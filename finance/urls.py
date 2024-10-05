from django.urls import path
from .views import IncomeListCreateView, BudgetListCreateView, SavingGoalListCreateView, ExpenseListCreateView

urlpatterns = [
    path('expenses/',ExpenseListCreateView.as_view(), name = 'expenses'),
    path('incomes/', IncomeListCreateView.as_view(), name='incomes'),
    path('budgets/', BudgetListCreateView.as_view(), name='budgets'),
    path('saving-goals/', SavingGoalListCreateView.as_view(), name='saving-goals')
]