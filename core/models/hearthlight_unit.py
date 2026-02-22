from django.db import models
from core.models.hearthlight_chapter import Chapter

# Create your models here.

    
class Unit(models.Model):
    name = models.CharField('Unit Name', max_length=100, unique=True)
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='chapter_units',
    )
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=9)
    country = models.CharField(max_length=100)
    blurb = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    # heraldry = models.ImageField(
    #     upload_to='unit_heraldry/',
    #     blank=True,
    #     null=True
    # )

    def __str__(self):
        return self.name