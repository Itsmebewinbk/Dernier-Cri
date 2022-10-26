from django.urls import path
from owner import views
urlpatterns = [
    path("index", views.AdminDashBoardView.as_view(), name="dashboard"),
    path("orders/latest", views.OrdersListView.as_view(), name="neworders"),
    path("orders/cancelled", views.OrderCancellationView.as_view(), name="order-cancelled"),
    path("orders/details/<int:id>", views.OrderDetailView.as_view(), name="order-details"),
    path("category/add", views.AddCategoryView.as_view(), name="add-category"),
    path("category/list", views.ListCategoryView.as_view(), name="list-category"),
    path("category/delete/<int:id>", views.delete_category, name="delete-category"),
    path("category/edit/<int:id>", views.EditCategoryView.as_view(), name="edit-category"),
    path("product/add", views.AddProductView.as_view(), name="add-product"),
    path("product/list", views.ListProducts.as_view(), name="list-product"),
]
