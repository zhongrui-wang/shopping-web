
from django.urls import path
from shoppingcart.views import add_to_cart, remove_from_cart, CartView, decreaseCart
from .views import Home
from .views import Shoes
from .views import Bags
from .views import PantsShorts
from .views import ShirtsSweatshirts
from .views import CoatsJackets
from .views import ProductDetail
from .views import SearchView


app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shoes', Shoes.as_view(), name='shoes'),
    path('bags', Bags.as_view(), name='bags'),
    path('pantsshorts', PantsShorts.as_view(), name='pantsshorts'),
    path('shirtssweatshirts', ShirtsSweatshirts.as_view(), name='shirtssweatshirts'),
    path('coatsjackets', CoatsJackets.as_view(), name='coatsjackets'),

    path('search', SearchView.as_view(), name='search'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('cart/', CartView, name='cart-home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]