from django.urls import path 
from . views import payment
from . views import success

app_name = "payment"

urlpatterns = [
	path('payment/', payment, name="payment"),
	path('success/', success, name="success")
]