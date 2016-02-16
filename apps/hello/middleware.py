from apps.hello.models import AllRequest


class RequestSaveMiddleware(object):
    """Display request time on a page"""

    def process_request(self, request):

        AllRequest(cookies_dict=str(request.COOKIES), url=request.path).save()
        return None
