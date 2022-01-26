from django.db import models


# Create your models here.

class contact_us(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده/نشده')

    class Meta:
        verbose_name = 'پیام ها'
        verbose_name_plural = 'پیام های کاربران'

    def __str__(self):
        return self.email
