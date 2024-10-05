from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Income, Expense, SavingGoal, Budget
from .serializers import ExpenseSerializer,IncomeSerializer,SavingGoalSerializer,BudgetSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
# We can use regular django views or use rest_framework capabilities
# Expense Views

class ExpenseListCreateView(APIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class IncomeListCreateView(APIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class SavingGoalListCreateView(APIView):
    queryset = SavingGoal.objects.all()
    serializer_class = SavingGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

class BudgetListCreateView(APIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

