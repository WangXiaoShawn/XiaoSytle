#在 Django 中，context_processors 是一种工具，它用于在每个模板的上下文中添加额外的数据。
#它们是一组可调用的函数，这些函数返回一个字典，字典中的每一项都会被添加到模板的上下文中。
#使用 context_processors，可以确保一些常用的数据在所有模板中都可用，而无需在每个视图中手动添加这些数据。
# 记得在seeting中的TEMPLATES中的context_processors中添加这个函数

from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0 #如果请求路径中包含 'admin'，则返回一个空字典。这通常是为了避免在管理后台页面计算购物车数量。
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request)) #尝试获取当前会话的购物车。如果购物车不存在，将捕获 Cart.DoesNotExist 异常。

            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
                
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count) #返回一个包含购物车商品数量的字典，键名为 cart_count。这个字典可以用于在模板中访问 cart_count 变量。



