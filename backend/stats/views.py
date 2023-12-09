from django.shortcuts import render
from transactions.models import Transaction
from stats.statistics import Statistics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from stats.serializers import StatisticsSerializer
from rest_framework_simplejwt import authentication as authjw

@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication, authjw.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class StatisticsListView(APIView):
    def get(self, request, budget_id):
        transactions = Transaction.objects.filter(account__owner=request.user, budget=budget_id).prefetch_related('tags')
        print(f"T: {transactions}")
        statistics = Statistics(transactions)
        print(statistics.to_dict())
        serialized_statistics = StatisticsSerializer(statistics.to_dict())

        return Response(serialized_statistics.data)