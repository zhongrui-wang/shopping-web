from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
# Create your models here.

User = get_user_model()
# Database of billing address 
class BillingAddress(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.user.username} billing address'

	class Meta:
		verbose_name_plural = "Billing Addresses"

class BillingForm(ModelForm):

	class Meta:
		model = BillingAddress
		fields = ['address', 'zipcode', 'city', 'state']

