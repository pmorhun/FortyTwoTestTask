import json
from django.core.urlresolvers import reverse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import RequestsLog


def requests_list(request):
    template_name = 'request_log/requests_list.html'

    requests_set = RequestsLog.objects.all()
    if len(requests_set.filter(status=False)) < 10:
        events = requests_set.filter(status=False).order_by('-id')[:10]
    else:
        events = requests_set.filter(status=False).order_by('-id')[:20]

    if len(requests_set) > 0:
        last_request = requests_set.latest('id').id
    else:
        last_request = 1

    context = {
        'events': events,
        'last_request': last_request,
    }
    return render(request, template_name, context)


def requests_list_ajax(request):
    if request.is_ajax():
        data = serializers.serialize("json", RequestsLog.objects.all().order_by('-id')[:10])
        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404




def mark_viewed(reguest):
    if request.method == 'POST' and request.is_ajax():
        viewed_l = request.POST.getlist('viewed[]')
        if len(viewed_l) > 0:
            RequestsLog.objects.filter(pk__in=viewed_l).update(status=True)

