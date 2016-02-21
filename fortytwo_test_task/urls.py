from django.conf.urls import patterns, include, url
from apps.contact.views import PersonView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PersonView.as_view(), name='contact'),
    url(r'^requests_list$', 'requests_list', name='requests_list'),

    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
