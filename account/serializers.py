from rest_framework import serializers
class DishSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digit=6,decimal_places=2)