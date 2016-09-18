from django.test import TestCase
from cStringIO import StringIO
from django.contrib.auth.models import User
import datetime

from books.models import Book, Bookshelf
from importer.importer import Importer

testImport = """ "_id","author_details","title","isbn","publisher","date_published","rating","bookshelf_id","bookshelf","read","series_details","pages","notes","list_price","anthology","location","read_start","read_end","format","signed","loaned_to","anthology_titles","description","genre","language","date_added","goodreads_book_id","last_goodreads_sync_date","last_update_date","book_uuid",
"1","Orwell, George","Animal Farm","9780140126709","Penguin Uk","1990-01-02","0","2,","Bookshelf,","0","","95","","","0","","","","Paperback","0","","","Desc","","English","2015-10-04 17:19:47","0","0000-00-00","2015-10-04 17:19:47","77894ecfab579372d2951bff6197b907",
"2","Wilde, Oscar|Koenig, Eva-Maria","Picture Of Dorian Gray., The","9783150090190","Reclam, Ditzingen","1995-06-01","0","1,2,","Schrank, Bookshelf,","0","Lernmaterialien","","","","0","","","","Paperback","0","","","","Desc","English","2015-10-04 17:20:37","0","0000-00-00","2015-10-04 17:20:37","16e18de057e4fb07bedad9856683590a",
"3","Twain, Mark|Boehnke, Reinhild","Knallkopf Wilson","9783717522003","Manesse Verlag","2010-03-01","0","2,","Bookshelf,","0","","317","","","0","","","","Hardcover","0","","","","","German","2015-10-04 17:21:02","0","0000-00-00","2015-10-04 17:21:02","7b99bf6965814ec9336f8035344ab4ef",
"""

class ImporterTestsCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.bs = Bookshelf.objects.create(user = self.u1, bc_export_id = 2, bc_name = "Bookshelf")

    def test_can_create_importer(self):
        inf = StringIO(testImport)
        Importer(self.u1)

    def test_basic_import(self):
        inf = StringIO(testImport)
        i = Importer(self.u1)
        i.readModelsFromFile(inf)
        self.assertEqual(len(i.books), 3)
        self.assertEqual(len(i.bookshelfs), 2)
        self.assertEqual(i.bookshelfs[2], self.bs)

        self.assertEqual(i.bookshelfs[1].bc_name, "Schrank")
        self.assertEqual(i.bookshelfs[1].user, self.u1)

    def _dateParseDateTest(self, s, r):
        i = Importer(None)
        self.assertEqual(i._parseDate(s), r)

    def test_date_empty(self):
        self._dateParseDateTest("", None)

    def test_date_garbage(self):
        self._dateParseDateTest("asdfer", None)

    def test_date_nulldate(self):
        self._dateParseDateTest("0000-00-00", datetime.date(1970,1,1))

    def test_date_three(self):
        self._dateParseDateTest("2016-08-12", datetime.date(2016,8,12))
    def test_date_two(self):
        self._dateParseDateTest("2016-08", datetime.date(2016,8,01))
    def test_date_one(self):
        self._dateParseDateTest("2016", datetime.date(2016,1,01))

    def test_datetime_garbage(self):
        i = Importer(None)
        self.assertEqual(i._dt("asdfer"), None)

    def test_datetime_valid(self):
        i = Importer(None)
        s ="2015-10-04 17:19:47"
        self.assertEqual(i._dt(s), datetime.datetime(2015,10,04,17,19,47))

    def tearDown(self):
        self.bs.delete()
        self.u1.delete()
