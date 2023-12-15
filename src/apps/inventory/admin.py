from django.contrib import admin

from src.apps.inventory.models import Category, Product, ProductImage


class ProductImageInline(
    admin.TabularInline
):  # or admin.StackedInline for a different layout
    model = ProductImage
    extra = 1  # Number of empty forms to display


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ["name", "category", "price", "stock", "in_stock"]
    list_filter = ["category", "in_stock"]
    search_fields = ["name", "category__name"]
    exclude = ["in_stock"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
