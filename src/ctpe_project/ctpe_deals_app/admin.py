from django.contrib import admin

from .models import *
# Register your models here.

class DealAdmin(admin.ModelAdmin):
	list_display = ['deal_name', 'for_category',]

admin.site.register(Category)
admin.site.register(Deal, DealAdmin)
admin.site.register(Tag)