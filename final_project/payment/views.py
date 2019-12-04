from django.shortcuts import render
from . models import PaymentInfoForm, PaymentInfo
from shoppingcart.models import Order, Cart
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def payment(request):

	# Checkout view
	form = PaymentInfoForm
	order = Order.objects.get(user=request.user, ordered=False)
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	# order_total = order_qs[0].get_totals() 
	context = {"form": form}
	# Getting saved payment 
	saved_payment = PaymentInfo.objects.filter(user = request.user)
	if saved_payment.exists():
		savedPayment = saved_payment.first()
		context = {"form": form, "savedPayment": savedPayment}
	if request.method == "POST":
		saved_payment = PaymentInfo.objects.filter(user = request.user)
		if saved_payment.exists():

			savedPayment = saved_payment.first()
			form = PaymentInfoForm(request.POST, instance=savedPayment)
			if form.is_valid():
				paymentinfo = form.save(commit=False)
				paymentinfo.user = request.user
				paymentinfo.save()
		else:
			form = PaymentInfoForm(request.POST)
			if form.is_valid():
				paymentinfo = form.save(commit=False)
				paymentinfo.user = request.user
				paymentinfo.save()
		cartItems = Cart.objects.filter(user=request.user)
		for cart_item in cartItems:
			cart_item.delete()		
		order = Order.objects.get(user=request.user, ordered=False)
		orderId = get_random_string(length=10, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		order.ordered = True
		order.paymentId = f'#{request.user}{orderId}'
		order.orderId = f'#{request.user}{orderId}'
		order.save()	
		return render(request, 'payment/success.html', context)
	return render(request, 'payment/payment.html', context)


def success(request):
	return render(request, 'payment/success.html', {"key": key, "total": total})