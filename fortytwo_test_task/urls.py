from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hello.views import PersonView, AllRequestView
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PersonView.as_view(), name='hello'),
    url(r'^all_requests$', AllRequestView.as_view(), name='all_requests'),
    url(r'^hello/(?P<pk>[0-9]+)/edit/$', 'apps.hello.views.person_edit', name='person_edit'),
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
