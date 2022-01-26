from django.contrib import admin
from .models import me, information, skills, Work, education, CV_file


# Register your models here.
class introduction_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = me.objects.all().count()
        if count == 0:
            return True
        return False


class cv_admin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = CV_file.objects.all().count()
        if count == 0:
            return True
        return False


class information_admin(admin.ModelAdmin):
    list_display = ['info', 'value']


class skills_admin(admin.ModelAdmin):
    list_display = ['title', 'done', 'others']
    list_filter = ['done', 'others']


admin.site.register(Work)
admin.site.register(education)
admin.site.register(CV_file, cv_admin)
admin.site.register(skills, skills_admin)
admin.site.register(me, introduction_admin)
admin.site.register(information, information_admin)
