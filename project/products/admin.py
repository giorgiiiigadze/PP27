from django.contrib import admin
from .models import Product


admin.site.site_header = "My shop Admin"
admin.site.site_title = "My shop portal"
admin.site.index_title = 'Welcome to my shop portal'

# ////////////////////////////////////////////////////////
# admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','price', 'in_stock')
#     list_filter= ('in_stock',)
#     search_fields = ('name',)
#     ordering = ('-name',)   # price
#     list_editable = ( 'in_stock',)

    # readonly_fields = ('price', )
    # fields = ('name','price', 'in_stock')   # edit formebistvisaa magram rame fieldtan shetanxmebit 
# ////////////////////////////////////////////////////////


@admin.action(description='mark selected products as out of stock')
def mark_out_of_stock(modeladmin, request, queryset):
    queryset.update(in_stock = False)

@admin.action(description='mark selected products as in  stock')
def mark_in_stock(modeladmin, request, queryset):
    queryset.update(in_stock = True)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'in_stock')
    list_filter= ('in_stock',)
    search_fields = ('name',)
    ordering = ('-name',)   # price
    # list_editable = ( 'in_stock',)

    # readonly_fields = ('price', )
    # fields = ('name','price', 'in_stock')   # edit formebistvisaa magram rame fieldtan shetanxmebit 
    actions = [mark_out_of_stock, mark_in_stock]