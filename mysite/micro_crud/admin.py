from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)