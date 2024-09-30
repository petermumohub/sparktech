from django.contrib import admin
from .models import Category,Subcategory, Product,ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3 

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(ProductImage)