from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    book_genre = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name
