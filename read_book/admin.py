from django.contrib import admin

from .models import Book, UserBookRelation, Comment, Genres

admin.site.register(Book)

admin.site.register(UserBookRelation)

admin.site.register(Comment)

admin.site.register(Genres)
