from django.db import models

class Chapter(models.Model):

    name = models.CharField('Chapter', max_length=100, unique=True)
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=9)
    country = models.CharField(max_length=100)
    blurb = models.TextField(blank=True)

    # heraldry = models.ImageField(
    #     upload_to='chapter_heraldry/',
    #     blank=True,
    #     null=True
    # )

    def __str__(self):
        return self.name