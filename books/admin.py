from django.contrib import admin
from .models import Book, Bookshelf
from django.forms import TextInput
from django.db import models

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }

admin.site.register(Bookshelf)

# Register your models here.
