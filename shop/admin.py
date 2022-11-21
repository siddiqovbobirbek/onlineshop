from django.contrib import admin

from .models import Category, ProductPhoto, Review, Brand, Product, Order, OrderDetail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category"""
    list_display = ("id", "name", "url", )
    list_display_links = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "product", "text", )
    readonly_fields = ("name", "email")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "description", "category", )
    list_display_links = ("name", "url", )


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ("url", "image", "category", )
    list_display_links = ("category", "image")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("url", "category", "name", "description", "brand", "price", "item",)
    list_display_links = ("name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "number", "email", "address", "datetime", "total",)
    list_display_links = ("number", "datetime")


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("url", "product", "order", "name", "price",)
    list_display_links = ("name", "product")
