from rest_framework import serializers
from translations.models import Transaction, Account, TransactionCategory, TransactionTag


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = '__all__'

class TransactionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTag
        fields = '__all__'
