import json
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import RequestsLog


def requests_list(request):
    template_name = 'request_log/requests_list.html'

    requests_set = RequestsLog.objects.all()
    if len(requests_set.filter(status=False)) < 10:
        events = requests_set.filter(status=False).order_by('-id')[:10]
    else:
        events = requests_set.filter(status=False).order_by('-id')

    if len(requests_set) > 0:
        last_request = requests_set.latest('id').id
    else:
        last_request = 1

    context = {
        'events': events,
        'last_request': last_request,
    }
    return render(request, template_name, context)


def requests_viewed(request):
    if request.is_ajax() and 'viewed[]' in request.POST:
        viewed_l = request.POST.getlist('viewed[]')
        if len(viewed_l) > 0:
            RequestsLog.objects.filter(pk__in=viewed_l).update(status=True)
    return HttpResponse(json.dumps({}), content_type='application/json')
