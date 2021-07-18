from django.contrib import admin
from .models import Posts
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display=('name','post','date','author','description','status')
admin.site.register(Posts,PostAdmin)
