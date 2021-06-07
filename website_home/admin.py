from django.contrib import admin
from .import models

class ArticleAdmin(admin.ModelAdmin):
    ...
    # your code here 
    ...

    class Media:
        js = ('ckeditor.js',)

admin.site.register(models.Categories)
admin.site.register(models.Products)
# Register your models here.
