from django.contrib import admin
from .models import Publication, UserPublicationRelation


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created', 'updated']
    list_filter = ('created',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'publication', 'like', 'bookmarked')


admin.site.register(Publication, PublicationsAdmin)
admin.site.register(UserPublicationRelation, LikeAdmin)

