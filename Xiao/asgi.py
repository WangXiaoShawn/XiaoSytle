"""
ASGI config for Xiao project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
作用：这个文件包含了项目的 ASGI（Asynchronous Server Gateway Interface）配置。ASGI 是用于处理异步请求的接口标准。
asgi.py 文件通常用于配置 Django 项目的异步能力，并用于部署异步应用。
"""



import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Xiao.settings')

application = get_asgi_application()
