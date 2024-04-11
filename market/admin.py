from django.contrib import admin

from market.models import Books


# Register your models here.
@admin.register(Books)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_count', 'category', 'author_name', 'image']
    search_fields = ['name', 'author_name']
    list_per_page = 10
