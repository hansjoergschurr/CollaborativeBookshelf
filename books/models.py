from django.db import models
from django.contrib.auth.models import User
import uuid

class Book(models.Model):
    user = models.ForeignKey(User)
    author_details = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=200)
    date_published = models.DateField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField() # rating from 0-5
    bookshelfs = models.ManyToManyField("Bookshelf", blank=True)
    read = models.BooleanField()
    series_details = models.CharField(max_length=200)
    pages = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField()
    list_price = models.PositiveIntegerField(null=True, blank=True)
    ANTHOLOGY_CHOICES = [
            ('0',"No."),
            ('1',"Yes, all by the same author."),
            ('2',"Yes, different authors.")
    ]
    anthology = models.BooleanField()
    location = models.CharField(max_length=200)
    read_start = models.DateField(null=True, blank=True)
    read_end = models.DateField(null=True, blank=True)
    book_format = models.CharField(max_length=200)
    signed = models.BooleanField()
    loaned_to = models.CharField(max_length=200)
    anthology_titles = models.CharField(max_length=400)
    description = models.TextField()
    genre = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    last_update_date = models.DateTimeField()
    uuid = models.UUIDField(default=uuid.uuid4)

class Bookshelf(models.Model):
    export_id = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
