from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


from accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

