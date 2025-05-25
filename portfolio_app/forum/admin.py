from django.contrib import admin
from forum.models import Category, Post, Reaction, ReactionType, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ReactionType)
admin.site.register(Reaction)