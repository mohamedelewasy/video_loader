from django.shortcuts import render
from .models import WebSite

def fun(request):
    websites = WebSite.objects.all()

    if request.method == 'POST':
        link = request.GET['video_link']

    return render(request, 'index.html', {'websites':websites})

