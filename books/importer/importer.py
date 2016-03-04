import csv
from books.models import Book
import datetime
import uuid

def parseDate(ds):
    if len(ds)==0:
        return None
    if ds=="0000-00-00":
        return datetime.date(1970,1,1)
    ds = ds.split('-')
    if len(ds)==3:
        return datetime.date(int(ds[0]),int(ds[1]),int(ds[2]))
    if len(ds)==2:
        return datetime.date(int(ds[0]),int(ds[1]),1)
    if len(ds)==1:
        return datetime.date(int(ds[0]),1,1)
    return None

def valueOrNull(s):
    if len(s)==0:
        return None
    else:
        return int(s)

def dt(s):
    datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")

def readRow(row):
    book = Book()
    book.bc_author_details = row['author_details']
    book.bc_title = row['title']
    book.bc_isbn = row['isbn']
    book.bc_publisher = row['publisher']
    book.bc_date_published_orig = row['date_published']
    book.bc_date_published = parseDate(row['date_published'])
    book.bc_rating = int(row['rating'])
    book.bc_read = bool(int(row['rating']))
    book.bc_series_details = row['series_details']
    book.bc_pages = valueOrNull(row['pages'])
    book.bc_list_price = row['list_price']
    book.bc_anthology = int(row['anthology'])
    book.bc_location = row['location']
    book.bc_read_start = parseDate(row['read_start'])
    book.bc_read_start_orig = row['read_start']
    book.bc_read_end = parseDate(row['read_end'])
    book.bc_read_end_orig = row['read_end']
    book.bc_book_format = row['format']
    book.bc_signed = bool(int(row['signed']))
    book.bc_loaned_to = row['loaned_to']
    book.bc_anthology_titles = row['anthology_titles']
    book.bc_description = row['description']
    book.bc_genre = row['genre']
    book.bc_language = row['language']
    book.bc_date_added =  dt(row['date_added'])
    book.bc_goodreads_bookid = int(row['goodreads_book_id'])
    book.bc_goodreads_sync_date = parseDate(row['last_goodreads_sync_date'])
    book.bc_last_update_date = dt(row['last_update_date'])
    book.bc_uuid = uuid.UUID(row['book_uuid'])

    # todo: bookshelf handling

def readModelsFromFile(csvfile):
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        book_model = readRow(row)
