from django.contrib import admin

from . models import *

class LawyersAdmin(admin.ModelAdmin):
    list_display = [ 'firstname', 'lastname', 'email', 'phone']


class UsersAdmin(admin.ModelAdmin):
    list_display = [ 'firstname', 'lastname', 'email', 'phone']



admin.site.register( Lawyers, LawyersAdmin)
admin.site.register(Users, UsersAdmin)