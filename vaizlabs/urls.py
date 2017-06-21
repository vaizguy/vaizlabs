from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Home
    url(r'^$', 'vaizlabs.apps.home.views.home', name='home'),
    url(r'^home$/', 'vaizlabs.apps.home.views.home', name='home'),
      
    # Blog 
    url(r'^blog', 'vaizlabs.apps.home.views.blog', name='blog'),

    # Contact 
    url(r'^contact$', 'vaizlabs.apps.home.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
]
