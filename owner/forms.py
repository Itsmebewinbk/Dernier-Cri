from django import forms
from owner.models import *


class OrderUpdateForm(forms.Form):
    options = (
        ("dispatched", "dispatched"),
        ("in-transit", "in-transit")
    )
    status = forms.ChoiceField(choices=options, widget=forms.Select(attrs={"class": "form-label"}))
    expected_delivery_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-label", "type": "date"}))


class CategoryForm(forms.ModelForm):
    # is forms.CharField(widgets=forms.TextInput(attrs={"class": "form-control"})
    class Meta:
        model = Categories
        fields = ["category_name","is_active"]
        widget = {
            "category_name" :forms.TextInput(attrs={"class": "form-control"})
        }


class ProductForm(forms.ModelForm):
            class Meta:
                model = Products
                fields = ["product_name","category","img","price","description"]
class EditCategoryForm(forms.ModelForm):
    class Meta:
        model= Categories
        fields= "__all__"
