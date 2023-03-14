from pyexpat import model
from rest_framework import serializers
from .models import GroceryCategory, Grocery

class GroceryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryCategory
        fields = "__all__"
    
class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = "__all__"


