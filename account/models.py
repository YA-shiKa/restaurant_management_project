from django.db import models
class Menu(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digit=5,decimal_place=2)
    def __str__(self):
        return self.name

class Order(models.Model):
    menu_item=models.ForeignKey(Menu,related_name='orders',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digit=6,decimal_place=2)

    def save(self,*args,**kwargs):
        self.total_price=self.menu_item.price*self.quantity
        super().save(*args,**kwargs)
    def __str__(self):
        return f"Order for {self.menu_item.name} (Quantity: {self.quantity})"