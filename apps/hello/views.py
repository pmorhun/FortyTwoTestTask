from django.shortcuts import render


def person(request):

    persons = {
                "bio": "I am Peter. Blah, blah, blah....",
                "first_name": "Petro",
                "last_name": "Morhun",
                "contacts": "https://www.facebook.com/petermorhun",
                "birthday": "1969-11-15",
                "skype": "p.etros",
                "jabber": "pmorhun@42cc.co ",
                "email": "petermorhun@gmail.com"
                },

    return render(request, 'hello/persons.html', {'persons': persons})
