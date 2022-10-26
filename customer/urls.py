from django.urls import path
from customer import views
urlpatterns = [
    path("register", views.RegistrationView.as_view(), name="register"),
    path("", views.LogInView.as_view(), name="login"),
    path("home", views.HomeView.as_view(), name="home"),
    path("logout", views.LogOutView.as_view(), name="logout"),
    path("products/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:id>/carts/add", views.AddToCartView.as_view(), name="add-to-cart"),
    path("carts/all", views.MyCartView.as_view(), name="mycart"),
    path("carts/placeorder/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place-order"),
    path("carts/remove/<int:id>",views.cart_item_remove,name="cart-item-remove"),

]
