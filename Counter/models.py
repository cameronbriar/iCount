from django.db import models

# Create your models here.

class Counter(models.Model):
    title = models.CharField(max_length=256, unique=True)
    count = models.IntegerField()

    def __unicode__(self):
        return "{0:>s} : {1:d}".format(self.title, self.count)