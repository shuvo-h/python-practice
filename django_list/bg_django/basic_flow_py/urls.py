"""
URL configuration for basic_flow_py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from machine_learning import urls as machine_urls
from blogs import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # use this routes whenever the url start with 'machine/'
    path('machine/', include((machine_urls, 'machine_learning'), namespace='machine_learning')),
    path('blogs/', include((blog_urls, 'blogs'), namespace='blogs')),

]
