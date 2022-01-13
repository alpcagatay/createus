from django.contrib import admin
from .models import MyClubUser
# Register your models here.
@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('user','role')
    search_fields = ('user',)