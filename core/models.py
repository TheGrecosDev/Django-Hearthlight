from django.db import models
from django.conf import settings

# Create your models here.


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
    
class Unit(models.Model):
    ...

class Member(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member',
    )
    contact_email = models.EmailField(max_length=254)
    chapter = models.ForeignKey(
        Chapter,                      # note: class, not Chapter()
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='chapter_members',       # optional but useful
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    game_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.game_name})"

