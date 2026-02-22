from django.db import models
from django.conf import settings
from core.models.hearthlight_chapter import Chapter

# Create your models here.

class Member(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='member',
    )
    contact_email = models.EmailField(max_length=254)
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='chapter_members',
    )
    game_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)
    country = models.CharField(max_length=100)

    def __str__(self):
        chapter_name = str(self.chapter) if self.chapter else "Chapterless"
        return f"{self.game_name or 'Unnamed'} ({self.user.first_name} {self.user.last_name}) of {chapter_name}"
