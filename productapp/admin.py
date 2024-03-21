from django.contrib import admin

# Register your models here.
from .models import Product,Category,Comment

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','is_published','created_at','price',)
    list_display_links=('id','name',)
    list_filter=('price',)
    list_editable=('is_published',)
    search_fields=('price','name',)
    ordering=('-price',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)