from django.contrib import admin
from blogs.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','blog_id','name','email','title','desc')
admin.site.register(Blog,BlogAdmin)  # it will display the blog table in admin anel