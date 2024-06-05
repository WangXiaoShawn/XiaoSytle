"""
WSGI config for greatkart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#SGI（Web Server Gateway Interface）是一种用于Python Web应用程序和Web服务器之间的接口标准。这个文件的主要目的是配置WSGI应用程序，以便Web服务器可以与Django项目通信。
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Xiao.settings')

application = get_wsgi_application()
