from django.contrib import admin
from games_crud.models import VideoGame, Publisher


# Register your models here.


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'listing_posted')
    readonly_fields = ('listing_posted',)
    list_filter = ('title', 'description')
    ordering = ('-listing_posted', 'title')

    fieldsets = (
        ('Basic data', {
            'fields': ('title', 'description',)
        }),
        ('Metadata', {
            'fields': ('listing_posted',)
        }),
    )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
