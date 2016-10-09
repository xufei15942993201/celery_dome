from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from celery_app import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celery_dome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index',views.index,name='index')
)
