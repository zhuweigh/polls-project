from django.conf.urls import patterns, include, url
from django.contrib import admin
#from users.admin import admin_site

#from  polls import urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
	#(r'^myadmin/', include(admin_site.urls)),
)
