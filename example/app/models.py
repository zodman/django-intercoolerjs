from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=30, help_text="Entry help text")

class Address(models.Model):
    street = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    line_one = models.TextField()
    number  = models.PositiveIntegerField()
