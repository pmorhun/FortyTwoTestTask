from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from fortytwo_test_task import settings
from apps.request_log.views import requests_list, requests_list_ajax
from apps.contact.views import edit_person
from apps.contact.views import PersonView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', PersonView.as_view(), name='contact'),
    url(r'^requests_list/$', requests_list, name='requests_list'),
    url(r'^requests_list_ajax/', requests_list_ajax),
    url(r'^edit_person/$', login_required(edit_person), name='edit_person'),

    # User Related urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name="contact_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'contact'}, name='contact_logout'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
