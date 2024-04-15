from django.contrib import admin
from django.utils.html import format_html_join

from market.models import Books, Category, Author


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Books)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_count', 'display_categories', 'author', 'image']
    search_fields = ['author__name', 'name']
    list_per_page = 10

    def display_categories(self, obj):
        return format_html_join(
            ', ', '{}', ((category.name,) for category in obj.category.all())
        )

    display_categories.short_description = 'Categories'
