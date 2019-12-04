# from django.shortcuts import render

# # Create your views here.
from django.views.generic import ListView, DetailView
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = Product
    template_name = 'products/home.html'

class Shoes(ListView):
    model = Product
    template_name = 'products/shoes.html'

class Bags(ListView):
    model = Product
    template_name = 'products/bags.html'

class PantsShorts(ListView):
    model = Product
    template_name = 'products/pantsshorts.html'

class ShirtsSweatshirts(ListView):
    model = Product
    template_name = 'products/shirtssweatshirts.html'

class CoatsJackets(ListView):
    model = Product
    template_name = 'products/coatsjackets.html'

class ProductDetail(DetailView, LoginRequiredMixin): #LoginRequiredMixin,
	model = Product

class SearchView(ListView):
    model = Product
    template_name = 'products/search.html'
    def get_queryset(self): 
        search = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=search)
        )
        return object_list
