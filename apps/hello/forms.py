from apps.hello.models import Person
from django.forms import ModelForm


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'birthday', 'bio',
                  'email', 'jabber', 'skype', 'contacts']
