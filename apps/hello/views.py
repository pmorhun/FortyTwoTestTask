from django.shortcuts import render

from django.views.generic import ListView
from apps.hello.models import Person


class PersonView(ListView):
    model = Person
    template_name = 'hello/persons.html'
    context_object_name = 'persons'

    def get_queryset(self):
        persons = Person.objects.all()
        return persons

