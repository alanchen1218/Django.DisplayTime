from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# from datetime import datetime

def index(request):
    # date = datetime.now().date().strftime('%B %-d, %Y')
    # time = datetime.now().time().strftime('%-I:%M %p')

    date = strftime('%B %-d, %Y', gmtime())
    time = strftime('%I:%M %p', gmtime())
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request,'time_display/index.html', context)