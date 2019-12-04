from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
# Create your models here.
User = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    # def get_total(self):
    #     return self.item.price * self.quantity
    # get each product's total price
    def get_total(self):
        total = self.item.price * self.quantity
        totalwithfloat = float("{0:.2f}".format(total)) #use float
        return totalwithfloat

class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=200, blank=True , null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    # get total price of all products in shopping cart
    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
        return total
    