from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40)
    discribe = models.TextField(max_length=1500, blank=True, null=True)
    cover = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    tags = models.ManyToManyField("books.Tag", related_name="book", blank=True)
    author = models.ForeignKey(
        'books.Author',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    on_shelf = models.BooleanField(db_column = "Czy na półce")

    def __str__(self):
        return f"id:{self.id}, Title:'{self.title}', Author:{self.author}, Cover:{self.cover}"

    class Meta:
        ordering = ["-id"]

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word
