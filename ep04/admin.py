from django.contrib import admin

from ep04.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', 'modified_at')
    search_fields = ('title',)
