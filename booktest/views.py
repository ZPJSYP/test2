from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import BookInfo
from datetime import date

# Create your views here.
from booktest import models


def index(request):
    book_list = models.BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'book_list': book_list})


def create(request):
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date.today()
    b.bcomment = 666
    b.bread = 999
    b.save()
    return HttpResponseRedirect('/books')
