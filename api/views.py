from django.shortcuts import render
from owner.models import *
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.viewsets import ModelViewSet
from api.serializer import *

class CategoryView(ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = CategorySerializer

class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = ProductSerializer


class CartsView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Carts.objects.filter(users=self.request.user)

class OrderView(ModelViewSet):
    queryset = Carts.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = OrderSerializer