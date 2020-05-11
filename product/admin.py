from django.contrib import admin
from .models import ItemModel, ImageModel
# Register your models here.


class ImageModelInline(admin.TabularInline):
    model = ImageModel
    extra = 1


class ItemModelAdmin(admin.ModelAdmin):
    inlines = [ImageModelInline]


admin.site.register(ItemModel, ItemModelAdmin)
admin.site.register(ImageModel)
