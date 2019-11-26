from django.shortcuts import render
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
import _nbatest
from pprint import pprint as pp
from player.models import player
from nba_api.stats.static import players
from datetime import datetime
from fusioncharts import FusionCharts
import json

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
        
        full_name = name.split(' ')
        first_name = ""
        last_name = ""
        context = {}
        results = {}
        print(full_name)
        if len(full_name) == 1:
            first_name = full_name[0]
            p1 = players.find_players_by_first_name(first_name)
            print("p1:", p1)

            for p in p1:
                results[p['full_name']] = p['full_name']
                
        elif len(full_name) == 2:
            first_name = full_name[0]
            last_name = full_name[1]
            p1 = players.find_players_by_first_name(first_name)
            p2 = players.find_players_by_last_name(last_name)
            print("p1:", p1)
            print("p2:", p2)

            for p in p1:
                results[p['full_name']] = p['full_name']
            for p in p2:
                results[p['full_name']] = p['full_name']

        #print('results', results)
        context['results'] = results
        print("context", context)
        return render(request, 'results.html', context=context)
     

    print("Got " + p.full_name)
    common_player_info = commonplayerinfo.CommonPlayerInfo(player_id=p.id, timeout=40, headers=header)
    common_player_info = common_player_info.get_normalized_dict()
    pi = common_player_info['CommonPlayerInfo'][0]
    ppgJson = _nbatest.queryPlayerPPGScrollGraph(p.id)
    fgpercent = _nbatest.queryPlayerFGPScrollGraph(p.id)
    logo_url = "img/Team_Logos/{}.png".format(str.lower(pi['TEAM_ABBREVIATION']))
    stat_table = _nbatest.queryTableInfo(p.id)
    scroll2D_1 = FusionCharts("scrollline2d", "Chart1", "600", "400", "chart-containter-1", "json", json.loads(ppgJson))
    scroll2d_2 = FusionCharts("scrollline2d", "Chart2", "600", "400","chart-container-2","json",json.loads(fgpercent))
    context = {
            'Logo_URL':logo_url,
            'Headshot_URL':"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{}.png".format(p.id),
            'Player_Name':p.full_name,
            'Player_Team_City' :pi['TEAM_CITY'],
            'Player_Team_Name': pi['TEAM_NAME'],
            'Player_Team_abbv':pi['TEAM_ABBREVIATION'],
            'Jersey_Number':pi['JERSEY'],
            'Player_Age':int(abs((datetime.now()-datetime.strptime(pi['BIRTHDATE'].split("T")[0],"%Y-%m-%d")).days)/365.24),
            'Player_Height':pi['HEIGHT'],
            'Player_Weight':pi['WEIGHT'],
            'chart1':scroll2D_1.render(),
            'chart2':scroll2d_2.render(),
            'stats':stat_table,
            

            
    }
    return render(request, 'player.html', context=context)


def aboutPage(request):
    return render(request, 'about.html')


def randomPage(request):
    return render(request, 'player.html', {'Player_Name': 'Random Player'})
