from django.contrib import admin
from .models import Member, Chapter

# Register your models here.

# Register Member
admin.site.register(Member)

# Register Chapter
admin.site.register(Chapter)

# # Register Unit
# admin.site.register(Unit)