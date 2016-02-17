from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from apps.hello.forms import PersonForm
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


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('hello')
    else:
        form = PersonForm(instance=person)
    return render(request, 'hello/person_form.html', {'form': form})
