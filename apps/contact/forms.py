from django.forms import ModelForm, DateInput
from apps.contact.models import Person


class ContactForm(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'birthday', 'photo', 'email',
                  'jabber', 'skype', 'other_contacts', 'bio')

        widgets = {'birthday': DateInput(attrs={'class': 'datepicker'})}
