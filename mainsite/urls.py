from django.urls import re_path

from .views import home, info, wishlist, location, contact, history



urlpatterns = [
    re_path('^$', home),
    re_path('info', info),
    re_path('wishlist', wishlist),
    re_path('location', location),
    re_path('contact', contact),
    re_path('history', history)
]
