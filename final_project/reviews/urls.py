from django.urls import path 
from . views import reviews, display

app_name = "reviews"

urlpatterns = [
	path('reviews/', reviews, name="reviews"),
    path('display/', display, name="display")
]