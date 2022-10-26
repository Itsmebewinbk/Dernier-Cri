from django.db import models
from django.contrib.auth.models import User
from  django.core.validators import MinValueValidator,MaxValueValidator

class Categories(models.Model):
    category_name=models.CharField(max_length=120,unique=True)
    is_active=models.BooleanField(max_length=120,default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=120,unique=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    img=models.ImageField(max_length=120,null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.product_name

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True,null=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(choices=options,max_length=120,default="in-cart")
    qty=models.PositiveIntegerField(default=1)

class Orders(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    options = (
        ("order-placed", "order-placed"),
        ("dispatch","dispatch"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(choices=options, max_length=120, default="order-placed")
    delivery_address=models.CharField(max_length=180,null=True)
    expected_delivery_date=models.DateTimeField(null=True)


class Reviews(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.CharField(max_length=120)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])





