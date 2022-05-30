from django.contrib import admin
from .models import About, AboutImages, Benefits, News, HelpImages, Help, Offer


class AboutInline(admin.TabularInline):
    fk_name = 'about'
    model = AboutImages
    max_num = 3


class AboutImage(admin.ModelAdmin):
    inlines = [AboutInline,]


admin.site.register(About, AboutImage)
admin.site.register(Benefits)
admin.site.register(News)
admin.site.register(HelpImages)
admin.site.register(Help)
admin.site.register(Offer)