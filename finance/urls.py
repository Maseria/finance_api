from django.urls import path
from .views import RegisterUser, IncomeListCreateView, BudgetListCreateView, SavingGoalListCreateView, ExpenseListCreateView

urlpatterns = [
    path('register/',RegisterUser.as_view(), name = 'register'),
    path('expenses/',ExpenseListCreateView.as_view(), name = 'expenses'),
    path('incomes/', IncomeListCreateView.as_view(), name='incomes'),
    path('budgets/', BudgetListCreateView.as_view(), name='budgets'),
    path('saving-goals/', SavingGoalListCreateView.as_view(), name='saving-goals')
]