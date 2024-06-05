# 这段代码定义了一个名为 menu_links 的上下文处理器（context processor）。上下文处理器是一种在所有模板中可用的全局上下文变量的机制。
# 具体来说，它允许你将某些数据添加到 Django 应用程序的所有模板的上下文中，而无需在每个视图中显式传递这些数据。

from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
