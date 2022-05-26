from django.contrib import admin
from .models import Product, CollectionProducts, ImageProducts, Slider


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ImageProducts
    max_num = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProducts)
admin.site.register(Slider)