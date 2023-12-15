from django.urls import path

from src.apps.inventory.views import ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog"),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        ProductDetailView.as_view(),
        name="product_page",
    ),
]
