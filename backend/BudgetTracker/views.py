# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag
# from .serializers import (
#     BudgetSerializer,
#     TransactionSerializer,
#     AccountSerializer,
#     TransactionCategorySerializer,
#     TransactionTagSerializer,
# )
# from .permissions import IsOwner
# # from .statistics import Statistics

# class BudgetListView(generics.RetrieveAPIView):
#     queryset = Budget.objects.all()
#     serializer_class = BudgetSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

# class BudgetDetailView(generics.RetrieveAPIView):
#     queryset = Budget.objects.all()
#     serializer_class = BudgetSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

# class TransactionListView(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

#     def perform_create(self, serializer):
#         serializer.save(account=self.request.user.account)

# class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]

# class BudgetCreateView(generics.CreateAPIView):
#     serializer_class = BudgetSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class TagCreateView(generics.CreateAPIView):
#     serializer_class = TransactionTagSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class CategoryCreateView(generics.CreateAPIView):
#     serializer_class = TransactionCategorySerializer
#     permission_classes = [permissions.IsAuthenticated]





from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag
# from .forms import TransactionForm, TagForm, CategoryForm, BudgetForm
from .statistics import Statistics
from datetime import datetime
from .serializers import (
    BudgetSerializer,
    TransactionSerializer,
    AccountSerializer,
    TransactionCategorySerializer,
    TransactionTagSerializer,
)

class BudgetDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, budget_id):
        budget = get_object_or_404(Budget, id=budget_id)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, budget_id):
        budget = get_object_or_404(Budget, id=budget_id)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(account__owner=request.user).prefetch_related('tags')
        statistics = Statistics(transactions)
        total_amount = statistics.calculate_total_amount()
        monthly_amounts = statistics.calculate_monthly_amounts()
        daily_amounts = statistics.calculate_daily_amounts()

        serializer = TransactionSerializer(
            transactions,
            many=True,
            context={'total_amount': total_amount, 'monthly_amounts': monthly_amounts, 'daily_amounts': daily_amounts}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TransactionDetailView(APIView):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    

class TransactionCategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        categories = TransactionCategory.objects.all()
        serializer = TransactionCategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id):
        category = get_object_or_404(TransactionCategory, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

