from django.db import models
from django.contrib.auth.models import User
import uuid

# fields starting with bc correspond to a book catalogue field
class Book(models.Model):
    user = models.ForeignKey(User)
    bc_author_details = models.TextField("Author Details")
    bc_title = models.TextField("Title")
    bc_isbn = models.TextField("ISBN",null=True, blank=True)
    bc_publisher = models.TextField("Publisher",null=True, blank=True)
    bc_date_published = models.DateField("Date Published",null=True, blank=True)
    bc_date_published_orig = models.TextField("Date Published Orig",null=True, blank=True)
    bc_rating = models.PositiveSmallIntegerField("Rating", default=0) # rating from 0-5
    bc_bookshelfs = models.ManyToManyField("Bookshelf", blank=True)
    bc_read = models.BooleanField("Read")
    bc_series_details = models.TextField("Series Details",null=True, blank=True)
    bc_pages = models.PositiveIntegerField("Pages",null=True, blank=True)
    bc_notes = models.TextField("Notes",null=True, blank=True)
    bc_list_price = models.TextField("List Price",null=True, blank=True)
    ANTHOLOGY_CHOICES = [
            (0,"No."),
            (1,"Yes, all by the same author."),
            (2,"Yes, different authors.")
    ]
    bc_anthology = models.IntegerField("Anthology",default=0, choices=ANTHOLOGY_CHOICES)
    bc_location = models.TextField("Location", null=True, blank=True)
    bc_read_start = models.DateField("Read Start",null=True, blank=True)
    bc_read_end = models.DateField("Read End",null=True, blank=True)
    bc_read_start_orig = models.TextField("Read Start Orig",null=True, blank=True)
    bc_read_end_orig = models.TextField("Read End Orig",null=True, blank=True)
    bc_book_format = models.TextField("Book Format", null=True, blank=True)
    bc_signed = models.BooleanField("Signed",default = False)
    bc_loaned_to = models.TextField("Loaned To", null=True, blank=True)
    bc_anthology_titles = models.TextField("Anthology Titles", null=True, blank=True)
    bc_description = models.TextField("Description", null=True, blank=True)
    bc_genre = models.TextField("Genre", null=True, blank=True)
    bc_language = models.TextField("Language", null=True, blank=True )
    bc_date_added = models.DateTimeField("Date Added")
    bc_goodreads_bookid = models.IntegerField("Goodreads Book ID", null=True, blank=True)
    bc_goodreads_sync_date = models.DateField("Goodreads Sync Date",null = True, blank=True)
    bc_last_update_date = models.DateTimeField("Update Date")
    bc_uuid = models.UUIDField("UUID",default=uuid.uuid4)

class Bookshelf(models.Model):
    bc_export_id = models.PositiveIntegerField("Export ID")
    bc_name = models.TextField("Name",null=True, blank=True)
