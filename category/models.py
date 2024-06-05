from django.db import models
from django.urls import reverse
#用于定义你的数据模型。模型定义了应用程序的数据结构，Django 会根据这些模型生成相应的数据库表。你可以在这个文件中定义模型类，并为每个类指定不同的数据字段
# Create your models here.

class Category(models.Model):
    # 这里本质就是建立数据库表的字段
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self): #使用 reverse 函数生成 URL，reverse 函数通过 URL 配置中的 products_by_category 视图名称和分类的 slug 作为参数来生成 URL
            #  return reverse('products_by_category', args=[self.slug])
            return reverse('products_by_category', args=[self.slug]) #products_by_category 来自于   这个是store 的 url path('<slug:category_slug>/', views.store, name='products_by_category'),


    def __str__(self):
        return self.category_name
