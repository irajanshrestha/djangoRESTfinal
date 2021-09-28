from .models import Data, Product
from rest_framework import serializers

class ProductViewSet(serializers.Modelserializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(serializers.Modelserializer):
    class Meta:
        model = Product
        fields = '__all__'
        