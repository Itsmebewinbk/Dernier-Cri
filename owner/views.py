from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from  django.contrib import messages
from owner.models import Orders, Carts,Products,Categories
from owner.forms import *
from owner import forms
from django.views.generic import *


class AdminDashBoardView(TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cnt1 = Orders.objects.filter(status="order-placed").count()
        cnt2 = Carts.objects.filter(status="cancelled").count()
        cnt3=Categories.objects.all().count()
        cnt4=Products.objects.all().count()
        context["count"] = cnt1
        context["cnt2"] = cnt2
        context["cnt3"] = cnt3
        context["cnt4"] = cnt4
        return context

class OrdersListView(ListView):
    model = Orders
    context_object_name = "orders"
    template_name = "admin-listorder.html"

    def get_queryset(self):
        return Orders.objects.filter(status='order-placed')


class OrderDetailView(DetailView):
    model = Orders
    template_name = "owner/order-details.html"
    pk_url_kwarg = "id"  # use self.get_object to call id in detail and update view
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["form"] = OrderUpdateForm()
        return context

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        form = OrderUpdateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("expected_delivery_date")
            order.status = form.cleaned_data.get("status")
            order.expected_delivery_date = form.cleaned_data.get("expected_delivery_date")
            order.save()
            send_mail(
                'order delivery update future store',
                f'your order will be delivered on {date}',
                'mindlesspeople1217@gmail.com',
                ['pratikshapoojari10@gmail.com'],
                fail_silently=True
            )
            print(form.cleaned_data)
            return redirect("dashboard")


class OrderCancellationView(ListView):
    model = Carts
    context_object_name = "orders"
    template_name = "cancelled-order.html"

    def get_queryset(self):
        return Carts.objects.filter(status='cancelled')

class AddCategoryView(CreateView):
    template_name = "add-category.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("list-category")

    def form_valid(self, form):
        messages.success(self.request, "Category Added")
        return super().form_valid(form)

class ListCategoryView(ListView):
    model = Categories
    context_object_name = "categories"
    template_name = "list-category.html"

def delete_category(reuqest,*args,**kwargs):
    id=kwargs.get("id")
    Categories.objects.get(id=id).delete()
    return redirect("list-category")

class EditCategoryView(UpdateView):
    model = Categories
    form_class = EditCategoryForm
    template_name = "edit-category.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("list-category")


class AddProductView(CreateView):
    model = Products
    template_name = "add-product.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("list-product")


class ListProducts(ListView):
    model = Products
    context_object_name = "product"
    template_name = "list-product.html"
