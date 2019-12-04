# from django.db import models

# # Create your models here.

from django.db import models

from django.urls import reverse

# Database of product
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()
    original_price = models.FloatField()
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("mainapp:product", kwargs={
            'slug': self.slug
        })
