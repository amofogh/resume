from django.contrib import admin

# Register your models here.
from social_media.models import social_media


class social_admin(admin.ModelAdmin):
    list_display = ['__str__', 'link']
    search_fields = ['title', 'link']


admin.site.register(social_media, social_admin)
