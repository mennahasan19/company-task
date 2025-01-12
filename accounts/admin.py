from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "role"]
    list_display_links = ["username", "email"]
