from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.datetime()#datetime.now().date().strftime('%B %-d, %Y')
    print date
    time = datetime.now().time().strftime('%-I:%M %p')
    context = {
        'datetime': [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request, 'times/index.html', context)

