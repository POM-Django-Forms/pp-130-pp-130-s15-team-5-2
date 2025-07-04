from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')
    fieldsets = (
        ('Author details', {'fields': ('name', 'surname'),
                            }),
    )


admin.site.register(Author, AuthorAdmin)
