from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'total_price')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    def items_display(self, obj):
        return ", ".join([str(item) for item in obj.items.all()]) 

    items_display.short_description = 'Items in Order'
    list_display += ('items_display',)

admin.site.register(Order, OrderAdmin)