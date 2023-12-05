from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework_simplejwt import authentication as authjw
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from transactions.models import Transaction,  TransactionCategory, TransactionTag
from datetime import datetime
from .serializers import (
    TransactionSerializer,
    AccountSerializer,
    TransactionCategorySerializer,
    TransactionTagSerializer,
)

@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication, authjw.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class TransactionListView(APIView):
    def get(self, request, budget_id):
        print(budget_id)
        transactions = Transaction.objects.filter(account__owner=request.user, budget=budget_id).prefetch_related('tags')
        serializer = TransactionSerializer(
            transactions,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication, authjw.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class TransactionDetailView(APIView):
    def get(self, request, budget_id, pk):
        transaction = get_object_or_404(Transaction, pk=pk, budget=budget_id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    
    def post(self, request, budget_id, pk):
        pass
    
@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication, authjw.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class TransactionCategoryView(APIView):
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
    
    def put(self, request):
        serializer = TransactionCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id):
        category = get_object_or_404(TransactionCategory, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication, authjw.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class TransactionTagView(APIView):
    def get(self, request):
        tags = TransactionTag.objects.all()
        serializer = TransactionTagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = TransactionTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tag_id):
        tag = get_object_or_404(TransactionTag, id=tag_id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)