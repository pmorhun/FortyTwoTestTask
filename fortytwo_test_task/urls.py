from django.conf.urls import patterns, include, url
from apps.contact.views import PersonView
from django.contrib import admin
from django.conf.urls.static import static
from fortytwo_test_task import settings
from apps.request_log.views import requests_list, requests_list_ajax
from apps.contact.views import edit_person

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PersonView.as_view(), name='contact'),
    url(r'^requests_list/$', requests_list, name='requests_list'),
    url(r'^requests_list_ajax/', requests_list_ajax),
    url(r'^edit_person/$', edit_person, name='edit_person'),

    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
