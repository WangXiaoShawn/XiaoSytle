from django.contrib import admin
from .models import Category

# Register your models here. 以下就相当于在后台加一个表头
class CategoryAdmin(admin.ModelAdmin):#定义一个自定义的管理类 CategoryAdmin，继承自 admin.ModelAdmin，用于定制 Category 模型在管理后台的显示和行为。
    prepopulated_fields = {'slug': ('category_name',)}#这里配置了 slug 字段应该根据 category_name 字段自动填充。当你在管理后台中输入 category_name 时，slug 字段会自动生成对应的 slug（通常是将空格替换为连字符，并将字符转换为小写）。
    list_display = ('category_name', 'slug') #用途：指定在管理后台的 Category 列表视图中显示哪些字段。


admin.site.register(Category,CategoryAdmin) # 这里注册了Category模型
