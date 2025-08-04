from django.db import models
from account.models import CustomUser
from products.models import Menu
class Order(models.Model):
    customer=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu,related_name='orders')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    order_status=models.CharField(max_length=50,choices=[('Pending','Pending'),('Completed'),('Completed')])

    def __str__(self):
        return f"Order {self.id}-{self.customer.username} ({self.order_status})"