from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','lists.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$','lists.views.view_list', name='view_list'),
    #url(r'^admin/', include(admin.site.urls)),
)
