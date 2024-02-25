from django.contrib import admin

# Register your models here.
from .models import Image
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']

admin.site.register(Image,ImageAdmin)