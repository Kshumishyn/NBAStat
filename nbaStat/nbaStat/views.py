from django.shortcuts import render


def homePage(request):
    return render(request, 'index.html')


def playerPage(request):
    print(type(request))
    name = request.GET.get('player_name')
    return render(request, 'player.html', {'Player_Name': name.title()})


def aboutPage(request):
    return render(request, 'about.html')


def randomPage(request):
    return render(request, 'player.html', {'Player_Name': 'Random Player'})
