from django.contrib import admin
from apps.hello.models import Person, AllRequest


# Register your models here.
admin.site.register(Person)
admin.site.register(AllRequest)
