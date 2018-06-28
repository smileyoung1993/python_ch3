"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import emaillist.views as emaillist_view
import guestbook.views as guestbook_view

urlpatterns = [
    path('admin/', admin.site.urls), # view 이름이 site

    path('emaillist/',emaillist_view.index), # viewfile은 templates 밑에 있다. views- > index함수 매핑
    path('emaillist/form',emaillist_view.form),
    path('emaillist/add',emaillist_view.add),

    path('guestbook/',guestbook_view.index)
]
