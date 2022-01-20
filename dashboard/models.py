from django.db import models

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    authors_info = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    price = models.FloatField()
    publish_date = models.IntegerField()

    def __str__(self):
        return self.book_title

    class Meta:
        ordering = ['authors_info']

class Logger(models.Model):
    log = models.CharField(max_length=1000)

class CrudLogger(models.Model):
    crud_log = models.CharField(max_length=1000, null=True, blank=True)
