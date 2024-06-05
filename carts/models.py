from django.db import models
from store.models import Product, Variation
from accounts.models import Account


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)#：如果一个 Account 对象被删除，所有引用该 Account 的记录（例如这个例子中的 user 字段）也会被删除。
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #：如果一个 Product 对象被删除，所有引用该 Product 的记录（例如这个例子中的 product 字段）也会被删除。
    variations = models.ManyToManyField(Variation, blank=True)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
