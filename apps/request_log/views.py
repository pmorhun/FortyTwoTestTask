from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import RequestsLog


def requests_list(request):
    template_name = 'request_log/requests_list.html'

    return render(request, template_name)


def requests_list_ajax(request):
    """ Ajax request """
    if request.is_ajax():
        events = RequestsLog.objects.all().order_by('-id')[:10]
        data = serializers.serialize("json", events)
        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404
