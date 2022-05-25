from django.contrib import admin
from .models import Product, CollectionProducts, ImageProducts


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ImageProducts
    

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProducts)