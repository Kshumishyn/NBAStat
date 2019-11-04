from django.shortcuts import render


def homePage(request):
    return render(request, 'index.html', {'Current_Name': 'Input a player Name'})


def playerPage(request):
    return render(request, 'player.html')
