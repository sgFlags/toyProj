from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_date', 'published_date', 'updated_date', 'status')
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('title', 'text')

admin.site.register(Post, PostAdmin)
