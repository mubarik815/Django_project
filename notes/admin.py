
from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_by',
        'is_done',
        'created_at',
        'created_day',

    )

    list_filter = ('is_done',)

    search_fields = (
        'title',
        'content',
        'created_by__username',
    )

    readonly_fields = (
        'created_by',
        'created_at',
    )

    def save_model(self, request, obj, form, change):
        # Automatically assign the logged-in admin
        # when creating a new note in Django Admin.
        if not change and obj.created_by_id is None:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)

