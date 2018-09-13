from django.contrib import admin
from main.models import BottomData


class BottomAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'color', 'sizes',)


# Register your models here.
admin.site.register(BottomData, BottomAdmin)
