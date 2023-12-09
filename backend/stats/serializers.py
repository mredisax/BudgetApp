from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    total_amount = serializers.FloatField()
    monthly_amounts = serializers.FloatField()
    daily_amounts = serializers.FloatField()

    class Meta:
        fields = ('total_amount', 'monthly_amounts', 'daily_amounts')