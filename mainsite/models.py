from django.db import models

# Create your models here.


class Wishlist(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(blank=True)
    picture_url = models.URLField(blank=True)
    text = models.TextField(max_length=1000)
    already_bought = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_bought = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PagesQuerySet(models.QuerySet):
    def page_with_path(self, page_path):
        return self.filter(path=page_path)

    def not_hidden(self):
        return self.filter(
            hidden=False
        )


class Page(models.Model):
    title = models.CharField(max_length=300)
    path = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    picture_url = models.URLField(blank=True)
    hidden = models.BooleanField(default=True)

    objects = PagesQuerySet.as_manager()

    def __str__(self):
        return self.title


