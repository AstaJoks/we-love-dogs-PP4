from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin Class for Contact Model
    """
    list_display = (
        'name',
        'reason',
        'email'
        )
    list_filter = (
        'name',
        'reason',
        'email',
    )
