from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
# Create your models here.

User = get_user_model()
# Database of reviews
class Reviews(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.CharField(max_length=30)
	comment = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.user.username} reviews'

	class Meta:
		verbose_name_plural = "Reviews"

class ReviewsForm(ModelForm):

	class Meta:
		model = Reviews
		fields = ['rating', 'comment']
