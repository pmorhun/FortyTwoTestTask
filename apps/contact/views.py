from django.views.generic import ListView
from apps.contact.models import Person


class PersonView(ListView):
    model = Person
    template_name = 'contact/contacts.html'
    context_object_name = 'person'

    def get_queryset(self):
        persons = Person.objects.get(id=1)
        return persons
