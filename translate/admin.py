from django.contrib import admin
from translate.models import Category, Band, Song, NewSong


class CategoryAdmin(admin.ModelAdmin):
    pass


class BandAdmin(admin.ModelAdmin):
    pass


class SongAdmin(admin.ModelAdmin):
    fields = ('name', 'name_ukr', 'text_ukr', 'text_org', 'likes', 'views', 'band', 'is_verified')
    list_display = ('name', 'name_ukr', 'text_ukr', 'text_org', 'likes', 'views', 'band', 'is_verified')


class NewSongAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ukr', 'text_org', 'text_ukr', 'user', 'verify_link')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(NewSong, NewSongAdmin)

