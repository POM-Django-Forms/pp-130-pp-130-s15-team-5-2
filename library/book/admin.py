from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'get_authors')
    list_filter = ('authors', 'name')
    search_fields = ('name',)
    fieldsets = (
        ('Immutable info', {'fields': ('name', 'authors'),
                            }),
        ('Mutable info', {'fields': ('count',),
                            }),
    )

    def get_authors(self, object):
        return ','.join([f'{a.name} {a.surname}' for a in object.authors.all()])
    get_authors.short_description = 'Authors'


admin.site.register(Book, BookAdmin)

