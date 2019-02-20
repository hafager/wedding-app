from django.shortcuts import render

# Create your views here.
from .models import Page
from .models import Wishlist


def home(request):
    pages = Page.objects.all()
    nav_pages = pages.not_hidden()
    page = pages.filter(path='home')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/home.html", {'nav_pages': nav_pages})


def info(request):
    nav_pages = Page.objects.not_hidden()
    page = nav_pages.filter(path='info')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/info.html", {'nav_pages': nav_pages, 'page': page})


def wishlist(request):
    wishes = Wishlist.objects.all()
    nav_pages = Page.objects.not_hidden()
    page = nav_pages.filter(path='wishlist')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/wishlist.html", {'nav_pages': nav_pages, 'page': page, 'wishes': wishes})


def location(request):
    nav_pages = Page.objects.not_hidden()
    page = nav_pages.filter(path='location')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/location.html", {'nav_pages': nav_pages, 'page': page})


def contact(request):
    nav_pages = Page.objects.not_hidden()
    page = nav_pages.filter(path='contact')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/contact.html", {'nav_pages': nav_pages, 'page': page})


def history(request):
    nav_pages = Page.objects.not_hidden()
    page = nav_pages.filter(path='history')
    if len(page) == 1:
        page = page[0]
    return render(request, "mainsite/history.html", {'nav_pages': nav_pages, 'page': page})
