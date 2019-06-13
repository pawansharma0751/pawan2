from django.contrib import admin
from firstapp.models import jaipurjobs

# Register your models here.
class jaipurjobsAdmin(admin.ModelAdmin):
    list_display=['company']
admin.site.register(jaipurjobs,jaipurjobsAdmin)
