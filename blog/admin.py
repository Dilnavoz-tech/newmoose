from django.contrib import admin
from django.contrib import admin
from .models import Post, Contact, Comment, Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_solved', 'created_at')
    list_display_links = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'author', 'view_count', 'created_at')
    list_display_links = ('id', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'is_visible', 'created_at')
    list_display_links = ('id', 'full_name')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)


