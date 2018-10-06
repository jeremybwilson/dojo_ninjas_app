# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DojoManager(models.Manager):
    def validate_and_create_dojo(self, form_data):
        errors = []

        name = form_data['name']
        city = form_data['city']
        state = form_data['state']
        desc = form_data['desc']

        if len(name) < 3:
            errors.append('Dojo Name should be more than three characers.')
        if len(city) < 3:
            errors.append('Dojo location should be more than three characers.')
        if len(state) < 2 or len(state) > 2:
            errors.append('Dojo state should be two characers.')

        dojo_list = Dojo.objects.filter(city=city)

        if len(dojo_list) > 0:
            errors.append('Dojo already exists in this city.')

        try:
            dojo = Dojo.objects.get(city=city)
            errors.append('City already has a Dojo.  Please choose another')
            return (False, errors)
        except:
            if len(errors) > 0:
                return (False, errors)
            else:
                dojo = Dojo.objects.create(name=name, city=city, state=state, desc=desc)
                return (True, dojo.id)

        return (True, dojo.id)

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default='', blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = DojoManager()

    def __str__(self):
        output = "<Dojo object: {} {}>".format(self.name, self.city)
        return output

class NinjaManager(models.Manager):
    def validate_and_create_ninja(self, form_data):
        if request.method == 'POST':
            errors = []
            if len(form_data['first_name']) < 3:
                errors.append('First name should be more than three characers.')
            if len(form_data['last_name']) < 3:
                errors.append('Last name should be more than three characers.')
            return errors

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    objects = NinjaManager()

    def __str__(self):
        output = "<Ninja object: {} {}>".format(self.first_name, self.last_name)
        return output
