from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, self.id)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category_detail", args=[str(self.slug)])


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    is_active = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock > 0:
            self.in_stock = True
        else:
            self.in_stock = False

        self.slug = slugify(self.name, self.id)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_page", args=[str(self.category.slug), str(self.slug)])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")
