from django.contrib import admin

from .models import ThriftUser

# Register your models here.
class ThriftUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'address', 'phone_no']
    list_display_links = ['id', 'email']
    list_filter = ['address', ]
    search_fields = ['email', 'address', 'phone_no']


admin.site.register(ThriftUser, ThriftUserAdmin)
