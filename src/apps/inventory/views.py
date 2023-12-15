from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from src.apps.inventory.models import Product, Category


class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_page.html"
    context_object_name = "product"
    slug_url_kwarg = "product_slug"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        category = get_object_or_404(Category, slug=category_slug)
        queryset = Product.objects.filter(category=category, is_active=True)
        return queryset

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock == 0:
            messages.error(self.request, "Out of stock")

        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = "inventory/catalog.html"
    context_object_name = "products"
