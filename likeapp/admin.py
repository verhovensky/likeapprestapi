from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'created_at', 'content_object')


admin.site.register(Like, LikeAdmin)
