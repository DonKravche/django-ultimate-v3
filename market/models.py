from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Author Name")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ManyToManyField(Category, verbose_name="Categories")
    author = models.ForeignKey(Author, verbose_name="Author Name", on_delete=models.CASCADE,
                               null=True, blank=True)

    name = models.CharField(max_length=255, verbose_name="Book Name")
    page_count = models.IntegerField(verbose_name="Number of Pages")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='Books/', null=True, blank=True, verbose_name="Book Image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id', 'name', 'price', 'page_count', 'author']
        indexes = [
            models.Index(fields=['id'], name='id'),
            models.Index(fields=['name'], name='name'),
            models.Index(fields=['price'], name='price'),
            models.Index(fields=['page_count'], name='page_count'),
            models.Index(fields=['author'], name='author')
        ]
        constraints = [
            models.UniqueConstraint(fields=['id', 'name', 'author'], name='unique_book')
        ]
