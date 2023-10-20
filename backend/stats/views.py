from django.shortcuts import render
from transactions.models import Transaction
from stats.statistics import Statistics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from stats.serializers import StatisticsSerializer


@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication])
@permission_classes([permissions.IsAuthenticated])
class StatisticsListView(APIView):
    def get(self, request):
        transactions = Transaction.objects.filter(account__owner=request.user).prefetch_related('tags')
        statistics = Statistics(transactions)
        serialized_statistics = StatisticsSerializer(statistics.to_dict())

        return Response(serialized_statistics.data)