from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from apps.contact.models import Person
from apps.contact.forms import ContactForm


class PersonView(ListView):
    model = Person
    template_name = 'contact/contacts.html'
    context_object_name = 'person'

    def get_queryset(self):
        person = Person.objects.get(id=1)
        return person


def edit_person(request):
    contact = get_object_or_404(Person)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse("redirect")
            else:
                return redirect(reverse('contact'))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_form.html', {'form': form})
