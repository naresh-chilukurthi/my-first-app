from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todolist(models.Model):
    name=models.CharField(max_length=60)
    creation_date=models.DateField()

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.name
class Todoitem(models.Model):
    description=models.CharField(max_length=150)
    duedate=models.DateField()
    Completed=models.BooleanField(default=False)
    owner=models.ForeignKey(Todolist)
    def __str__(self):
        return self.description