from django.contrib import admin


from core.models import (
    Chapter,
)

# Register Chapter
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    admin_section = 'Hearthlight'