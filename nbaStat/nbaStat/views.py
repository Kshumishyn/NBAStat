from django.shortcuts import render
from nba_api.stats.endpoints import commonplayerinfo

from player.models import player

header = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://stats.nba.com',

}


def homePage(request):
    return render(request, 'index.html')


def playerPage(request):
    name = request.GET.get('player_name')
    p = player.objects.get(full_name__iexact=name)
    print(p.full_name)
    
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=p.id, timeout= 40, headers = header)
    player_info = player_info.get_normalized_dict()
    context = {}
    d = player_info['CommonPlayerInfo'][0]    
    context = {
             'Player_Name': p.full_name,
             'Player_Team' : d['TEAM_CITY'] + " " + d['TEAM_NAME'],
             'Jersey_Number':d['JERSEY'],

    }
    return render(request, 'player.html', context=context)


def aboutPage(request):
    return render(request, 'about.html')


def randomPage(request):
    return render(request, 'player.html', {'Player_Name': 'Random Player'})
