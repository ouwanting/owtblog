from django.contrib import admin

# Register your models here.

from owtblog.models import Blogpost

class Blogpostadmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blogpost,Blogpostadmin)
