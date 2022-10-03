from django.contrib import admin
from books.models import Book, Tag, Author

# Register your models here.



class BookAdmin(admin.ModelAdmin):
   list_display = ['title', 'discribe', 'cover', 'author', 'on_shelf']
   list_filter = ['author', 'tags', 'on_shelf']
   search_fields = ['author', 'tags', 'on_shelf']

class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'first_name', 'last_name']

class TagAdmin(admin.ModelAdmin):
   list_display = ['word']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)