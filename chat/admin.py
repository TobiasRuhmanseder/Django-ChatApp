from .models import Chat, Message
from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
    fields = (
        "chat",
        "text",
        "created_at",
        "author",
        "receiver",
    )  # cutom display of data field / default u don' need this - use only admin.site.register(Message)
    list_display = ("text", "created_at", "author", "receiver")
    search_fields = ("created_at",)  # sorts the table depending on the input parameters


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
