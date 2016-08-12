import csv
from books.models import Book, Bookshelf
import datetime
import uuid

class Importer:
    def __init__(self, user):
        self.user = user
        self.bookshelfs = {}
        self.books = []

    def _parseDate(self, ds):
        if len(ds)==0:
            return None
        if ds=="0000-00-00":
            return datetime.date(1970,1,1)
        ds = ds.split('-')
        try:
            if len(ds)==3:
                return datetime.date(int(ds[0]),int(ds[1]),int(ds[2]))
            if len(ds)==2:
                return datetime.date(int(ds[0]),int(ds[1]),1)
            if len(ds)==1:
                return datetime.date(int(ds[0]),1,1)
        except ValueError:
            pass
        return None

    def _valueOrNull(self, s):
        if len(s)==0:
            return None
        else:
            return int(s)

    def _dt(self, s):
        try:
            return datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None

    def _readRow(self, row):
        book = Book()
        book.bc_author_details = row['author_details']
        book.bc_title = row['title']
        book.bc_isbn = row['isbn']
        book.bc_publisher = row['publisher']
        book.bc_date_published_orig = row['date_published']
        book.bc_date_published = self._parseDate(row['date_published'])
        book.bc_rating = int(row['rating'])
        book.bc_read = bool(int(row['rating']))
        book.bc_series_details = row['series_details']
        book.bc_pages = self._valueOrNull(row['pages'])
        book.bc_list_price = row['list_price']
        book.bc_anthology = int(row['anthology'])
        book.bc_location = row['location']
        book.bc_read_start = self._parseDate(row['read_start'])
        book.bc_read_start_orig = row['read_start']
        book.bc_read_end = self._parseDate(row['read_end'])
        book.bc_read_end_orig = row['read_end']
        book.bc_book_format = row['format']
        book.bc_signed = bool(int(row['signed']))
        book.bc_loaned_to = row['loaned_to']
        book.bc_anthology_titles = row['anthology_titles']
        book.bc_description = row['description']
        book.bc_genre = row['genre']
        book.bc_language = row['language']
        book.bc_date_added =  self._dt(row['date_added'])
        book.bc_goodreads_bookid = int(row['goodreads_book_id'])
        book.bc_goodreads_sync_date = self._parseDate(row['last_goodreads_sync_date'])
        book.bc_last_update_date = self._dt(row['last_update_date'])
        book.bc_uuid = uuid.UUID(row['book_uuid'])

        shelf_ids = self._getBookshelfs(row['bookshelf_id'], row['bookshelf'])
        return book

    def _getBookshelfs(self, bookshelf_ids, bookshelf_names):
        bookshelf_ids = bookshelf_ids.split(',')
        bookshelf_names = bookshelf_names.split(',')

        b = []
        for (i,n) in zip(bookshelf_ids, bookshelf_names):
            try:
                bookshelf_id = int(i)
                if not bookshelf_id in self.bookshelfs:
                    bookshelf = None
                    try:
                        bookshelf = Bookshelf.objects.get(bc_export_id = bookshelf_id, user = self.user)
                        bookshelf.bc_name = n
                    except Bookshelf.DoesNotExist:
                        bookshelf = Bookshelf(bc_export_id = bookshelf_id, bc_name = n, user = self.user)
                    self.bookshelfs[bookshelf_id] = bookshelf
                b.append(bookshelf_id)
            except ValueError:
                    pass
        return b

    def readModelsFromFile(self, csvfile):
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            book_model = self._readRow(row)
            self.books.append(book_model)
