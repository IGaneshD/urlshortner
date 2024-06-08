from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.URLField(max_length = 200, blank=False, null = False)
    shortLink = models.TextField(unique=True, max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.shortLink)
    
