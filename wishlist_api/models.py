from django.db import models

"""
User
    first_name
    last_name
    email
    password
Book
    title
    author
    isbn
    date of publication
"""


class Book(models.Model):
    owner = models.ForeignKey('auth.User',
                              related_name='books',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, blank=True, default='')
    date_pub = models.DateField(editable=True,
                                blank=True,
                                null=True)
