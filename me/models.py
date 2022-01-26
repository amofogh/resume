from django.db import models
from os import path
from django_jalali.db import models as jmodels


# Create your models here.
def get_filename(filepath):
    basename = path.basename(filepath)
    name, ext = path.splitext(basename)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename(filename)

    new_name = f'{instance.name}{ext}'
    return f'{new_name}'


class me(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    picture = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='عکس رزومه')
    job = models.CharField(max_length=200, verbose_name='سمت شغلی')
    phone = models.CharField(blank=True, null=True, max_length=100, verbose_name='شماره تلفن')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    about_me = models.TextField(verbose_name='درباره من')

    class Meta:
        verbose_name = 'مشخصات اصلی'
        verbose_name_plural = 'مشخصات اصلی'

    def __str__(self):
        return self.name


class information(models.Model):
    info = models.CharField(max_length=150, verbose_name='مشخصه')
    value = models.TextField(verbose_name='مقدار')

    class Meta:
        verbose_name = 'اطلاعات فرد'
        verbose_name_plural = 'اطلاعات فردی'

    def __str__(self):
        return self.info


class skills(models.Model):
    title = models.CharField(max_length=150, verbose_name='مهارت')
    done = models.BooleanField(default=True, verbose_name='تمام شده/نشده')
    others = models.BooleanField(default=False, verbose_name='مهارت نامرتبط')

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.title


class Work(models.Model):
    job = models.CharField(max_length=200, verbose_name='سمت شغلی')
    corp = models.CharField(max_length=200, verbose_name='نام شرکت')
    start = jmodels.jDateField(verbose_name='تاریخ شروع همکاری')
    check_now = models.BooleanField(default=False, verbose_name='تا الان')
    end = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ پایان همکاری(اگر تا الان هست خالی بزار)')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'سابقه شغلی'
        verbose_name_plural = 'سوابق شغلی'
        # abstract = True

    def __str__(self):
        return self.job


class education(models.Model):
    grade = models.CharField(max_length=200, verbose_name='مقطع تحصیلی')
    major = models.CharField(max_length=200, verbose_name='رشته درسی')
    place = models.CharField(max_length=200, blank=True, null=True, verbose_name='محل تحصیل')
    start = jmodels.jDateField(verbose_name='تاریخ شروع')
    check_now = models.BooleanField(default=False, verbose_name='تا الان')
    end = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ پایان (اگر تا الان هست خالی بزار)')

    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'سوابق تحصیلی'
        # abstract = True

    def __str__(self):
        return self.grade


class CV_file(models.Model):
    cv_file = models.FileField(verbose_name='فایل رزومه')

    class Meta:
        verbose_name = 'فایل رزومه'
        verbose_name_plural = 'فایل رزومه'
        # abstract = True

    def __str__(self):
        return 'فایل رزومه'
