from django.shortcuts import render
from budgets.models import Budget
from rest_framework import status, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
# Create your views here.

from .serializers import BudgetSerializer

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
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
