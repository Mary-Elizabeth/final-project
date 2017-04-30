"""db_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin


from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
     url(r'^madlib1/madlib1Filled/$', views.madlib1Filled, name='madlib1Filled'),
    url(r'^madlib1/$', views.madlib1, name='madlib1'),
    url(r'^madlib2/madlib2Filled/$', views.madlib2Filled, name='madlib2Filled'),
    url(r'^madlib2/$', views.madlib2, name='madlib2'),
    url(r'^madlib3/madlib3Filled/$', views.madlib3Filled, name='madlib3Filled'),
    url(r'^madlib3/$', views.madlib3, name='madlib3'),
    url(r'^admin/', admin.site.urls),
]
