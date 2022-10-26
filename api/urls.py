from api.views import ProductsView,CategoryView
from rest_framework.routers import DefaultRouter              #Modelviewset is routed by Default router class
router=DefaultRouter()
router.register("Category",CategoryView,basename="Category")
router.register("Products",ProductsView,basename="Product")
router.register("Carts",ProductsView,basename="Carts")
router.register("Orders",ProductsView,basename="Orders")
urlpatterns=[

]+router.urls