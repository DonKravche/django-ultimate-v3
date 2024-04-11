from django.db import models


# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=255, verbose_name="Book Name")
    page_count = models.IntegerField(verbose_name="Number of Pages")
    category = models.CharField(max_length=50, choices=[
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('children', 'Children\'s'),
    ])
    author_name = models.CharField(max_length=255, verbose_name="Author Name")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='Books/', null=True, blank=True, verbose_name="Book Image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id', 'name', 'price', 'page_count', 'author_name']
        indexes = [
            models.Index(fields=['id'], name='id'),
            models.Index(fields=['name'], name='name'),
            models.Index(fields=['price'], name='price'),
            models.Index(fields=['page_count'], name='page_count'),
            models.Index(fields=['author_name'], name='author_name')
        ]
        constraints = [
            models.UniqueConstraint(fields=['id', 'name', 'author_name'], name='unique_book')
        ]
