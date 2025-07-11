from django.db import models


# Create your models here.
class ContactUs(models.Model):
    TYPE_CHOICES = (
        ('counseling', 'مشاوره'),
        ('message', 'ارتباط با ما')
    )

    name = models.CharField(max_length=255, verbose_name='نام')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='نوع پیام')
    phone_number = models.CharField(max_length=255, verbose_name='شماره تماس')
    industry = models.CharField(max_length=255, verbose_name='زمینه فعالیت')
    message = models.CharField(max_length=255, null=True, blank=True, verbose_name='متن پیام')
    seen = models.BooleanField(default=False, verbose_name='خوانده شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = '1. تماس ها'

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
