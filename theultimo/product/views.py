from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from product.models import Product, Item
# Create your views here.


def product_list(request):
	queryset = Product.objects.all()

	context = {
		"object_list": queryset,
		"title": "Product"
	}

	return render(request, "product.html", context)

def home(request):
	queryset = Product.objects.all()

	context = {
		"object_list": queryset,
		"title": "Product"
	}

	return render(request, "index.html", context)
def about(request):
	return render(request,"about-us.html")

def item_list(request, product):
	queryset = Item.objects.filter(product = product)
	instance = get_object_or_404(Product, id =product)

	context = {

		"object_list" : queryset,
		"instance" : instance
	}

	return render(request, "item.html", context)

