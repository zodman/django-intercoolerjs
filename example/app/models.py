from django.db import models

class Entry(models.Model):
    name = models.CharField(unique=True, max_length=30, help_text="Entry help text")

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(unique=True, max_length=30)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    line_one = models.TextField()
    number  = models.PositiveIntegerField()
