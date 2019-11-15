from django.shortcuts import render
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats

from player.models import player
from datetime import datetime

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
    
    # Tries to Query by player's full name
    try:
        p = player.objects.get(full_name__iexact=name)
    except:
        print("Failed to get " + name)
        return render(request, 'index.html')

    print("Got " + p.full_name)
    common_player_info = commonplayerinfo.CommonPlayerInfo(player_id=p.id, timeout=40, headers=header)
    common_player_info = common_player_info.get_normalized_dict()
    pi = common_player_info['CommonPlayerInfo'][0]
    context = {
            'Player_Name':p.full_name,
            'Player_Team' :pi['TEAM_CITY'] + " " + pi['TEAM_NAME'],
            'Jersey_Number':pi['JERSEY'],
            'Player_Age':int(abs((datetime.now()-datetime.strptime(pi['BIRTHDATE'].split("T")[0],"%Y-%m-%d")).days)/365.24)
    }
    return render(request, 'player.html', context=context)


def aboutPage(request):
    return render(request, 'about.html')


def randomPage(request):
    return render(request, 'player.html', {'Player_Name': 'Random Player'})
