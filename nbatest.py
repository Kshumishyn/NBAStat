from nba_api.stats.static import players 
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
name = 'DISPLAY_FIRST_LAST'
ht = 'HEIGHT'

def main():
    player_info=commonplayerinfo.CommonPlayerInfo(player_id=2544)
    d = player_info.get_normalized_dict()
    print(d, "\n\n")
  #  print(d['CommonPlayerInfo'])
 #   print(type(d['CommonPlayerInfo']))
#    print(*d['CommonPlayerInfo'][0], sep= "\n")
    
    print(d['CommonPlayerInfo'][0]['DISPLAY_FIRST_LAST'], "#" ,d['CommonPlayerInfo'][0]['JERSEY'])
    print(d['CommonPlayerInfo'][0]['TEAM_CITY'], d['CommonPlayerInfo'][0]['TEAM_NAME'])
    print("Height:", d['CommonPlayerInfo'][0]['HEIGHT'])
    print("Number of Seasons:", d['CommonPlayerInfo'][0]['SEASON_EXP'])


# these are different ways to get available seasons from different players
#    player_info.available_seasons.get_json()
#    player_info.available_seasons.get_dict()
#    player_info.available_seasons.get_data_frame()

    # A dict of all available seasons for Lebron James
    d2 = player_info.available_seasons.get_dict()
    print("\n\n")
#    print("A dict of all available_seasons for Lebron James")
#    print(d2)
#    print("\n")


#    print(d2['data'][1][0])


    # Career stats for Lebron James
    career = playercareerstats.PlayerCareerStats(player_id=2544)
    # 
    d3 = career.get_dict()
    #print(d3['resultSets'][1])# This gets a dict of the careertotalRegularstats
    
    #Post season totals per season
    # - Includes 'headers': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

    # - Includes 'rowSet' : Includes the data matching the headers in sequence, returns a list of all seasons the player played in the post seasons
    print(d3['resultSets'][2], "\n\n")
    
    # Just the headers
    print(d3['resultSets'][2]['headers'], "\n\n"


)
    # Just the rowSet: A list of all seasons the player was in the post season with all of the stats mentioned previously in the 'headers' section
 #   for items in d3['resultSets'][2]['rowSet']:
#        print(items, "\n")
#        print(d3['resultSets'][2]['rowSet'])

    # Just the 2017-2018 season for Lebron James
    print(d3['resultSets'][2]['rowSet'][12])

    
    


if __name__ == '__main__':
    main()
