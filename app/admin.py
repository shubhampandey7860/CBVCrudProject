from django.contrib import admin
from app.models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','password']