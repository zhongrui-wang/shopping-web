from django.shortcuts import render
from . models import Reviews, ReviewsForm
from shoppingcart.models import Order, Cart
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
# from django.utils.crypto import get_random_string

# Create your views here.

def reviews(request):

	form = ReviewsForm
	order_qs = Order.objects.filter(user= request.user, ordered=False)
	# order_items = order_qs[0].orderitems.all()
	context = {"form": form}
	# Getting saved address
	saved_reviews = Reviews.objects.filter(user = request.user)
	if request.method == "POST":
		# saved_reviews = Reviews.objects.filter(user = request.user)
		# if saved_reviews.exists():
		# 	savedReviews = saved_reviews.first()
		# 	form = ReviewsForm(request.POST, instance=savedReviews)
		# 	if form.is_valid():
		# 		reviews = form.save(commit=False)
		# 		reviews.user = request.user
		# 		reviews.save()
		# else:
		form = ReviewsForm(request.POST)
		if form.is_valid():
			reviews = form.save(commit=False)
			reviews.user = request.user
			reviews.save()	
		messages.warning(request, "Saved Sccessfully")	
		return redirect("reviews:reviews")	
	return render(request, 'reviews/reviews.html', context)

def display(request):

    reviews = Reviews.objects.all()
    return render(request, 'reviews/display.html', {"reviews": reviews})

