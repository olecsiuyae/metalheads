from django.contrib import admin
from translate.models import Category, Band, Song


class CategoryAdmin(admin.ModelAdmin):
    pass


class BandAdmin(admin.ModelAdmin):
    pass


class SongAdmin(admin.ModelAdmin):
    fields = ('text_ukr', 'text_org', 'name', 'likes', 'views', 'band')
    list_display = ('text_ukr', 'text_org', 'name', 'likes', 'views', 'band')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Song, SongAdmin)


