from django.contrib import admin

# Register your models here.
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Body', {'fields': ['pub_date', 'text'], 'classes': ['collapse']}),
    ]

admin.site.register(Note, NoteAdmin)
