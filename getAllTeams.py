import json
from nba_api.stats.endpoints import commonplayerinfo as api
from pprint import pprint

players = json.loads(open("./All_Players.json").read())
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
teams = []
for player in players:
    print("Fetching team for {}".format(player["full_name"]))
    info = api.CommonPlayerInfo(player["id"],headers=header)
    team_id = info.get_normalized_dict()["CommonPlayerInfo"][0]["TEAM_ABBREVIATION"]
    if team_id not in teams:
        teams.append(team_id)
    print("{} team is {}".format(player["full_name"],team_id))
pprint(teams)
json.dumps(open("./team.json").write())
