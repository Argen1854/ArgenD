from django.contrib import admin
from .models import Product, CollectionProducts, ImageProducts, Slider, CallBack


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ImageProducts
    max_num = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
    fields = ['title', 'text', 'vendor_code', 'size_range', 'cloth', 'quantity_in_line', 'material', 'checkbox_hit', 'checkbox_new', 'collection', 'price', 'discount']

class CallBackAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)
    list_display = ('name', 'data')


admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProducts)
admin.site.register(Slider)
admin.site.register(CallBack, CallBackAdmin)