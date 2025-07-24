from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Columns to show in admin list view
    list_filter = ('role',)          # Filter by role
    search_fields = ('user__username',)  # Allow searching by username

# Register your models here.
