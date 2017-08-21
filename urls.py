#定义owtblog的url模式

from django.conf.urls import url
from . import views as owtblog_views
import re

urlpatterns=[url(r'^$',owtblog_views.Index,name='index'),
              url(r'^topics/$',owtblog_views.topics,name='topics'),
             ]
