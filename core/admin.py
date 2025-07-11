from django.contrib import admin

from core.models import ContactUs


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'phone_number', 'industry', 'seen')
    list_editable = ('seen',)
    list_filter = ('seen', 'created_at')
    search_fields = ('name', 'phone_number', 'industry')
    readonly_fields = ('created_at',)
