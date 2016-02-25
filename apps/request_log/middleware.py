from .models import RequestsLog


class RequestsLogMiddleware(object):
    def process_request(self, request):
        log_event = RequestsLog.objects.create(
            method=request.method, path=request.path)
        log_event.save()
        return None
