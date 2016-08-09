from django.test import TestCase
from cStringIO import StringIO
from django.contrib.auth.models import User

from books.models import Book
from importer.importer import Importer

testImport = """ "_id","author_details","title","isbn","publisher","date_published","rating","bookshelf_id","bookshelf","read","series_details","pages","notes","list_price","anthology","location","read_start","read_end","format","signed","loaned_to","anthology_titles","description","genre","language","date_added","goodreads_book_id","last_goodreads_sync_date","last_update_date","book_uuid",
"1","Orwell, George","Animal Farm","9780140126709","Penguin Uk","1990-01-02","0","2,","Bookshelf,","0","","95","","","0","","","","Paperback","0","","","Desc","","English","2015-10-04 17:19:47","0","0000-00-00","2015-10-04 17:19:47","77894ecfab579372d2951bff6197b907",
"2","Wilde, Oscar|Koenig, Eva-Maria","Picture Of Dorian Gray., The","9783150090190","Reclam, Ditzingen","1995-06-01","0","1,2,","Schrank, Bookshelf,","0","Lernmaterialien","","","","0","","","","Paperback","0","","","","Desc","English","2015-10-04 17:20:37","0","0000-00-00","2015-10-04 17:20:37","16e18de057e4fb07bedad9856683590a",
"3","Twain, Mark|Boehnke, Reinhild","Knallkopf Wilson","9783717522003","Manesse Verlag","2010-03-01","0","2,","Bookshelf,","0","","317","","","0","","","","Hardcover","0","","","","","German","2015-10-04 17:21:02","0","0000-00-00","2015-10-04 17:21:02","7b99bf6965814ec9336f8035344ab4ef",
"""

class ImporterTestsCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')

    def test_can_create_importer(self):
        inf = StringIO(testImport)
        Importer(self.u1)

    def test_basic_import(self):
        inf = StringIO(testImport)
        i = Importer(self.u1)
        i.readModelsFromFile(inf)

    def tearDown(self):
        self.u1.delete()
