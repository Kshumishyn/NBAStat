from django.shortcuts import render

def homePage(request):
    return render(request, 'index.html')

def playerPage(request):
    return render(request, 'player.html')
