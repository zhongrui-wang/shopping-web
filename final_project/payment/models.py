from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
# Create your models here.

User = get_user_model()
# Database of paymentinfo
class PaymentInfo(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cardnum = models.CharField(max_length=50)
	cvv = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.user.username} payment info'

	class Meta:
		verbose_name_plural = "Payment Info"

class PaymentInfoForm(ModelForm):

	class Meta:
		model = PaymentInfo
		fields = ['cardnum', 'cvv']