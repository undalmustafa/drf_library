from django.db import models
import uuid
from autoslug import AutoSlugField
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    book_genre = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='book_name')

    def __str__(self):
        return self.book_name