from django.contrib import admin

from .models import Category, ProductPhoto, Review, Brand, Product, Order, OrderItem, Xususiyatlari


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
    list_display = ("name", "url", "description", )
    list_display_links = ("name", "url", )


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "product" )
    list_display_links = ("image", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("url", "name", "brand", "price")
    list_display_links = ("url", "name")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "complete", "transaction_id")
    list_display_links = ("complete", "transaction_id")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product", "order", "quantity")
    list_display_links = ("product", "order")


@admin.register(Xususiyatlari)
class XususiyatlariAdmin(admin.ModelAdmin):
    list_display = ("vazni", "razmeri", "os_versiyasi", "protsessor", "product")
    list_display_links = ("vazni", "razmeri", "protsessor", "product")