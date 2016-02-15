from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hello.views import PersonView
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PersonView.as_view(), name='hello'),

    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
