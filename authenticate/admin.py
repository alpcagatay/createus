from django.contrib import admin
from .models import MyClubUser, UserStory
# Register your models here.
@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('user','role')
    search_fields = ('user',)
admin.site.register(UserStory)