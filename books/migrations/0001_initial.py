# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField()),
                ('author_details', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=200)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('read', models.BooleanField()),
                ('series_details', models.CharField(max_length=200)),
                ('pages', models.PositiveIntegerField(null=True, blank=True)),
                ('notes', models.TextField()),
                ('list_price', models.PositiveIntegerField(null=True, blank=True)),
                ('anthology', models.BooleanField()),
                ('location', models.CharField(max_length=200)),
                ('read_start', models.DateField(null=True, blank=True)),
                ('read_end', models.DateField(null=True, blank=True)),
                ('book_format', models.CharField(max_length=200)),
                ('signed', models.BooleanField()),
                ('loaned_to', models.CharField(max_length=200)),
                ('anthology_titles', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField()),
                ('last_update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('export_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookshelfs',
            field=models.ManyToManyField(to='books.Bookshelf', blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
