from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', view = blog_post_list, name='list'),
    url(r'^create/$', view = blog_post_create),
    url(r'^(?P<slug>[\w-]+)/$', view = blog_post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', view = blog_post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', view = blog_post_delete, name='deletepost'),
]
