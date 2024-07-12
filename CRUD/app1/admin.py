from django.contrib import admin
from .models import Books
# Register your models here.
@admin.register(Books)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','reg','title','issued','author','availability')