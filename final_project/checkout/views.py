
import uuid
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from shoppingcart.models import Order, Cart
from . models import BillingForm, BillingAddress
from django.views.generic.base import TemplateView


# Create your views here.
def checkout(request):

	form = BillingForm
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	# order_items = order_qs[0].orderitems.all()
	order_total = order_qs[0].get_totals() 
	context = {"form": form, "order_total": order_total}
	# Getting saved address
	saved_address = BillingAddress.objects.filter(user = request.user)
	if saved_address.exists():
		savedAddress = saved_address.first()
		context = {"form": form, "order_total": order_total, "savedAddress": savedAddress}

	if request.method == "POST":
		saved_address = BillingAddress.objects.filter(user = request.user)
		if saved_address.exists():
			savedAddress = saved_address.first()
			form = BillingForm(request.POST, instance=savedAddress)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()
		else:
			form = BillingForm(request.POST)
			if form.is_valid():
				billingaddress = form.save(commit=False)
				billingaddress.user = request.user
				billingaddress.save()	
		messages.warning(request, "Saved Sccessfully")	
		return redirect("checkout:index")	
	return render(request, 'checkout/index.html', context)


def orderView(request):

	try:
		orders = Order.objects.filter(user=request.user, ordered=True)
		context = {
			"orders": orders
		}
		if request.method == 'POST':
			order = Order.objects.filter(user=request.user, ordered=True) 
			order.delete()
			messages.info(request, f"{order.orderId} has deleted.")
			# return redirect("/my-orders")
	except:
		messages.warning(request, "You do not have an active order")
		return redirect('/my-orders')
	return render(request, 'checkout/order.html', context)




