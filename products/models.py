from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    datae = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.name)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveBigIntegerField(blank = True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return " solled {} - {} items for {} ".format(self.product.name,self.quantity
        ,self.total_price)




