from django.contrib import admin
from translate.models import Category, Band, Song, Page


class CategoryAdmin(admin.ModelAdmin):
    pass
class BandAdmin(admin.ModelAdmin):
    pass
class SongAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Page)

