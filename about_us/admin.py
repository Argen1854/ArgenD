from django.contrib import admin
from .models import About, AboutImages, Benefits, News, HelpImages, Help, Offer


class AboutInline(admin.TabularInline):
    fk_name = 'about'
    model = AboutImages
    max_num = 3


class AboutImage(admin.ModelAdmin):
    inlines = [AboutInline,]


class HelpH(admin.TabularInline):
    model = Help


class HelpHelp(admin.ModelAdmin):
    inlines = [HelpH,]



admin.site.register(About, AboutImage)
admin.site.register(Benefits)
admin.site.register(News)
admin.site.register(HelpImages, HelpHelp)
admin.site.register(Offer)