from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^css/(.*)','cms_users_put.views.servircss'),
    url(r'^plantilla/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': settings.STATIC2_URL}),
    url(r'^(.*)$', 'cms_users_put.views.cms_users_put'),
)
