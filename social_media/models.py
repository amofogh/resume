from django.db import models


# Create your models here.

class social_media(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام شبکه اجتماعی')
    link = models.URLField(verbose_name='لینک کاربر', unique=True)
    icon_tag = models.CharField(max_length=300, verbose_name='تگ ایکون (font awesome)')

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.title
