from django.contrib import admin

# Register your models here.


from .models import Product, Item


class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["title","image", "timestamp", "updated"]	
	search_fields = ["title"]
	list_filter = ["timestamp"]
	

	

	class Meta:
		model = Product

class ItemModelAdmin(admin.ModelAdmin):
	list_display = ["title", "product", "updated"]	
	search_fields = ["title"]
	list_filter = ["timestamp"]

	class Meta:
		model = Item


fields = ( 'image_tag', )
readonly_fields = ('image_tag',)

admin.site.register(Product, ProductModelAdmin)
admin.site.register(Item, ItemModelAdmin)
		



