from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def bookList(request):
    return HttpResponse("Books!")
