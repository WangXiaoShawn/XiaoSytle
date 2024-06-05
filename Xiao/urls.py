"""Xiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #admin：导入 Django 管理后台模块。
from django.urls import path, include #path 和 include：导入用于定义 URL 路径的函数。
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')), # 把admin映射到admin_honeypot
    path('securelogin/', admin.site.urls), # change the admin URL to something else
    path('', views.home, name='home'), # 这里指向了home函数
    path('store/', include('store.urls')),#含义：这是 URL 路径的一部分。当用户访问 http://yourdomain.com/store/ 时，这个路径会匹配这个配置。
    #Django 将所有以 /store/ 开头的 URL 请求交给 store.urls 模块处理。
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
     # ORDERS
    path('orders/', include('orders.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 这里是为了让media文件能够在浏览器中显示出来
#这段代码的配置确保了在开发环境中，用户可以通过指定的 URL 访问上传的媒体文件，同时定义了首页和管理后台的 URL 路径映射。如果你有更多问题或需要进一步的解释，请随时告诉我。
