from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'logins.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teams/', include('teams.urls')),
    url(r'^leagues/', include('leagues.urls')),
    url(r'^register/$', 'logins.views.register', name='register'),
    url(r'^login/$', 'logins.views.user_login', name='user_login'),
    url(r'^logout/$', 'logins.views.user_logout', name='user_logout'),
)
