"""lulu_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
                       url('^$', 'introPage.views.leaveContactInfo'),
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^static/(?P<path>/*)$', 'django.views.static.serve',
                       #    {'document_root': 'C:\Users\Ryan\Desktop\lulu_new\introPage'}),
                       url(r'^leaveContactInfo/$', 'introPage.views.leaveContactInfo'),
                       #url(r'^test/$', 'singleSlot.views.singleSlotStep'),
                       #url(r'^realtest/$','singleSlot.views.test'),
)
