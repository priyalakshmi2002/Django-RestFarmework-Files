from rest_framework import serializers
from .models import *

class Products_Serializers(serializers.ModelSerializer):
    category_reference = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),required=True,
                            error_messages={"required": "Category reference is required"})
    product_name = serializers.CharField(required=True,max_length=200,
                            error_messages={"required": "Product name is required","max_length":"Should exceed 200 characters"})
    code = serializers.CharField(required=True,max_length=100,
                            error_messages={"required": "Code is required","max_length":"Should exceed 100 characters"})
    price = serializers.FloatField(min_value=0,
                            error_messages={"min_value": "Price must be equla to or greater than 0"})
    class Meta:
        model = Products
        fields = '__all__'
        
    def validate_code(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Code should be alphanumeric.")
        return value
            
    def validate(self, data):
        if not data.get("category_reference"):
            raise serializers.ValidationError("Each product must be associated with a category.")
        return data

class GoldAPIValidationSertilaizer(serializers.Serializer):
    gold_type= serializers.CharField(required=True,max_length=100,source='title')
    gold_price_today=serializers.CharField(required=True,max_length=10,source='price')
    gold_rate_diff = serializers.CharField(required=True,max_length=5,source='difference')
    

# class Products_Serializers2(serializers.ModelSerializer):
    
#     class Meta:
#         model = Products
#         fields = ['product_name']
        
class Category_Serializer(serializers.ModelSerializer):
    category_name = serializers.CharField(required=True,max_length=200,
                        error_messages={"required": "Category name is required","max_length": "Category name should not exceed 200 characters"})
    class Meta:
        model = Category
        fields = '__all__'
    
    def validate_category_name(self, value):
        if Category.objects.filter(category_name=value).exists():
            raise serializers.ValidationError("This category name already exists.")
        return value
             
    #Nested serializer    
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']

# class ProductSerializer(serializers.ModelSerializer):
#     # Nested serializer
#     category = CategorySerializer()

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'price', 'category']
