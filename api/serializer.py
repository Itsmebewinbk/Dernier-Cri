from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from owner.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    users=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    quantity=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["user",
                "product",
                "created_date",
                "status",
                "qty"]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(user=user,product=product,**validated_data)
class OrderSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Orders
        fields=[
            "user",
            "product",
            "status"
        ]
    def create(self,validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Orders.objects.create(user=user,product=product,**validated_data)