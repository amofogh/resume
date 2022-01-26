from django.contrib import admin

# Register your models here.
from contact_us.models import contact_us


@admin.action(description='تغییر به خوانده شده')
def make_read(modeladmin, request, queryset):
    queryset.update(is_read=True)


@admin.action(description='تغییر به خوانده نشده')
def make_unread(modeladmin, request, queryset):
    queryset.update(is_read=False)


class contact_us_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'text']
    actions = [make_read, make_unread]


admin.site.register(contact_us, contact_us_admin)
