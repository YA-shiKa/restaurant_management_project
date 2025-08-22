from django.db import models
from django.contrib.auth.models import User 
from account.models import Menu

class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]
    customer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu,related_name='orders')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    order_status=models.CharField(max_length=50,choices=[('Pending','Pending'),('Completed'),('Completed')])

    def __str__(self):
        return f"Order #{self.id} for {self.customer.username} - ({self.order_status})"
    def calculate_total(self):
        total=sum(item.price for item in self.order_items.all())
        self.total_amount=total
        self.save()

    def save(self,*args,**kwargs):
        self.calculate_total()
        super(Order,self).save(*args,**kwargs)