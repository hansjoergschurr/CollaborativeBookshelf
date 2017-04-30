# Collaborative Bookshelf
This project aims to provide groups of friends the a convenient way to share their book collections among each other. 
Users share their collection by importing from the [Book Catalogue](https://github.com/eleybourn/Book-Catalogue) app.

Because of time constraints, the project currently lies dormant. For now consider using [Inventaire.io](https://inventaire.io) which is a mature project with a simmilar goal. 

# Development
If you want to try out the current development version of the project, first 
ensure that python3 is installet. Then run the following commands in the root
directory of the project:

```
source env/bin/activate
pip install -r requirements.txt
./manage.py makemigrations books
./manage.py migrate
./manage.py createsuperuser 
./manage.py runserver
```

and navigate your browser to (http://localhost:8000).
