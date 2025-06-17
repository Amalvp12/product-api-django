from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product          # tell DRF we’re translating Product objects
        fields = '__all__'       # include every field (name, category, price)
