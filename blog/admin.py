from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ('title', 'author', 'status')
    list_filter = ('author',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
