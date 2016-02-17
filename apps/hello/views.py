from django.shortcuts import render


def person(request):

    return render(request, 'hello/persons.html', {})

