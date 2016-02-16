from django.views.generic import ListView
from apps.hello.models import Person, AllRequest


class PersonView(ListView):
    model = Person
    template_name = 'hello/persons.html'
    context_object_name = 'persons'

    def get_queryset(self):
        persons = Person.objects.all()
        return persons


class AllRequestView(ListView):
    model = AllRequest
    template_name = 'hello/all_requests.html'
    context_object_name = 'requests'

    def get_queryset(self):
        requests = AllRequest.objects.all().order_by('-date')[:10]
        return requests
