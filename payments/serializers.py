from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
