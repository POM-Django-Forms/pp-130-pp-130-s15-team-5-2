from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_info', 'book_info', 'created_at', 'plated_end_at', 'end_at', 'is_closed')
    list_filter = ('created_at', 'plated_end_at', 'book', 'user')
    search_fields = ('user__email', 'book__name')
    readonly_fields = ('created_at',)

    def is_closed(self, obj):
        return obj.end_at is not None

    is_closed.boolean = True
    is_closed.short_description = 'Closed'

    def book_info(self, object):
        authors = ', '.join(f'{author.name} {author.surname}' for author in object.book.authors.all())
        return f"{object.book.name} ({authors})"

    book_info.short_description = 'Book'

    def user_info(self, object):
        return f"{object.user.first_name} {object.user.last_name} ({object.user.email})"

    user_info.short_description = 'User Info'


admin.site.register(Order, OrderAdmin)
