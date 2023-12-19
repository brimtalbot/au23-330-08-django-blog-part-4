from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    exclude = ('posts',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]
# Register your models here.
