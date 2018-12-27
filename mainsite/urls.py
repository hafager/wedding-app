from django.conf.urls import url

from .views import home, info, wishlist, location, contact



urlpatterns = [
    url('^$', home),
    url('info', info),
    url('wishlist', wishlist),
    url('location', location),
    url('contact', contact)
]