from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_date')
    list_filter = ("category",)
    search_fields = ['title', 'description']
  
admin.site.register(Blog, BlogAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ("stock",)
    search_fields = ['name', 'stock']
  
admin.site.register(Product, ProductAdmin)

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ("email",)
    search_fields = ['name', 'email']
  
admin.site.register(Contactus, ContactusAdmin)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Blogcategory)
admin.site.register(Aboutus)
admin.site.register(Partner)