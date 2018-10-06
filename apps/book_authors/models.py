# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from ..first_app.models import Dojo

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        output = "<Book object: {} {}>".format(self.name, self.desc)
        return output

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    books = models.ManyToManyField(Book, related_name = "authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    output = "<Author object: {} {} {}>".format(self.first_name, self.last_name, self.email)
    return output