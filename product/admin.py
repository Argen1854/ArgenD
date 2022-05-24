from django.contrib import admin
from .models import Product, CollectionProducts, ImageProducts, ColorProducts


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ImageProducts


class ColorInline(admin.TabularInline):
    fk_name = 'product'
    model = ColorProducts


class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ColorInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProducts)