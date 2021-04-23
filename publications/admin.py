from django.contrib import admin
from .models import Publication


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created', 'updated']
    list_filter = ('created',)


# class LikesAdmin(admin.ModelAdmin):
#     list_display = ['owner', 'created']
#     list_filter = ('created',)



admin.site.register(Publication, PublicationsAdmin)
# admin.site.register(Like, LikesAdmin)
