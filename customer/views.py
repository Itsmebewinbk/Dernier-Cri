from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from customer import forms
from django.urls import reverse_lazy
from owner.models import Products,Carts,Orders
from django.contrib.auth.models import User


class RegistrationView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "your account has been created")
        return super().form_valid(form)


class LogInView(FormView):  # formview:used to render form withount using get
    template_name = "login.html"
    form_class = forms.LogInForm

    def post(self, request, *args, **kwargs):
        form = forms.LogInForm(request.POST, files=request.FILES)
        # POST:charactervalue,files=request.FILES: Image ,django returns request.data so no need to give like this
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    return redirect("home")
            else:
                return render(request, "login.html", {"form": form})
        return render(request, "login.html")


class LogOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request, )
        return redirect("login")


class HomeView(TemplateView):
    template_name: str = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_product = Products.objects.all()
        context["products"] = all_product
        return context


class ProductDetailView(DetailView):
    template_name = "product-detail.html"
    model = Products
    context_object_name = "product"
    pk_url_kwarg = "id"


class AddToCartView(FormView):
    template_name = "add-to-cart.html"
    form_class = forms.CartsForm

    def form_valid(self, form):  # To save user
        form.instance.user = self.request.user
        messages.success(self.request, "Product has been added")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        product = Products.objects.get(id=id)

        return render(request, self.template_name, {"form": forms.CartsForm(), "product": product})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        products = Products.objects.get(id=id)
        qty = request.POST.get("qty")
        user = request.user
        Carts.objects.create(product=products, user=user, qty=qty)
        messages.success(request, "Product have been added succesfully!")
        return redirect("home")
    # def get_context_data(self, **kwargs):         #to send extra context
    #     context=super().get_context_data(**kwargs)
    #     return context


class MyCartView(ListView):
    model = Carts
    template_name = "cart-list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")  # (-) minus for getting order in decending order


def cart_item_remove(request, *args, **kwargs):
    cart_id = kwargs.get("id")
    cart = Carts.objects.get(id=cart_id)
    cart.status = "cancelled"
    cart.save()
    messages.success(request, "Item removed....")
    return redirect("mycart")


class PlaceOrderView(FormView):
    template_name = "place-order.html"
    form_class = forms.OrderForm

    def post(self, request, *args, **kwargs):
        cart_id = kwargs.get("cid")
        product_id = kwargs.get("pid")
        cart = Carts.objects.get(id=cart_id)
        product = Products.objects.get(id=product_id)
        user = request.user
        delivery_address = request.POST.get("delivery_address")
        Orders.objects.create(product=product, user=user, delivery_address=delivery_address)
        cart.status = "order-placed"
        cart.save()
        return redirect("home")
