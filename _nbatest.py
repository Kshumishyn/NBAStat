from nba_api.stats.static import players 
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
name = 'DISPLAY_FIRST_LAST'
ht = 'HEIGHT'

def main():
    # this is how you get commonplayer info
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
    player_info=commonplayerinfo.CommonPlayerInfo(player_id=2544, timeout=35, headers=header)
    # alternatively you can do this:
    # player_info=commonplayerinfo.CommonPlayerInfo(player_id=2544)
    # Just a dict of the commonplayer info:
    # Common Player Info Includes:
    # -- CommonPlayerInfo -- USEFUL
    # -- PlayerHeadlineStats -- COULD BE USEFUL
    # -- AvailableSeasons -- JUST A LIST OF SEASON
    d = player_info.get_normalized_dict()
    for items in d:
        print(items, "\n")
    print("\n")
    
    # Common Player Info Includes:
    # -- PERSON_ID -- USEFUL!!!!!!!!!!!!1
    # -- FIRST_NAME
    # -- LAST_NAME
    # -- DISPLAY_FIRST_LAST
    # -- DISPLAY_LAST_COMMA_FIRST
    # -- DISPLAY_FI_LAST
    # -- BIRTHDATE
    # -- SCHOOL -- REFERS TO COLLEGE -- THIS CAN BE WONKY, SHOULDN'T USE
    # -- COUNTRY
    # -- LAST_AFFLIATION -- REFERS TO COLLEGE/HIGHSCHOOL?
    # -- HEIGHT
    # -- WEIGHT
    # -- SEASON_EXP -- NUMBER OF SEASONS PLAYED
    # -- JERSEY
    # -- POSITION 
    # -- ROSTERSTATUS -- ACTIVE/NOTACTIVE
    # -- TEAM_ID
    # -- TEAM_ABBREVIATION
    # -- TEAM_CODE 
    # -- TEAM_CITY
    # -- PLAYERCODE -- NEED TO LOOK MORE AT THIS ONE
    # -- FROM_YEAR
    # -- TO_YEAR
    # -- DLEAGUE_FLAG -- 'Y'/'N' FOR EX. LEBRON IS NOT IN THE DLEAGUE SO 'N'
    # -- NBA_FLAG -- 'Y'/'N' LEBRON IS 'Y'
    # -- GAMES_PLAYED_FLAG -- NEED TO LOOK MORE AT THIS ONE
    # -- DRAFT_YEAR 
    # -- DRAFT_ROUND
    # -- DRAFT_NUMBER    
    print(d['CommonPlayerInfo'], "\n")
    # EXAMPLE OF HOW TO QUERY STUFF TO PRINT A PLAYER'S COMMON INFO
    print(d['CommonPlayerInfo'][0]['DISPLAY_FIRST_LAST'], "#" ,d['CommonPlayerInfo'][0]['JERSEY'])
    print(d['CommonPlayerInfo'][0]['TEAM_CITY'], d['CommonPlayerInfo'][0]['TEAM_NAME'])
    print("Height:", d['CommonPlayerInfo'][0]['HEIGHT'])
    print("Number of Seasons:", d['CommonPlayerInfo'][0]['SEASON_EXP'])
    print("\n\n")


    # these are different ways to get available seasons from different players
    # player_info.available_seasons.get_json()
    # player_info.available_seasons.get_dict()
    # player_info.available_seasons.get_data_frame()
    # A dict of all available seasons for Lebron James
    d2 = player_info.available_seasons.get_dict()
    print("\n\n")
    print("A dict of all available_seasons for Lebron James")
    print(d2)
    print("\nPrinting a specific season_id")
    print(d2['data'][1][0])
    # This part of the API is nice for quickly querying which seasons a 
    # player has played.
    # HOWEVER, it does nothing more than give you the number of the
    # specific season to query another part of the API. 
    # In other words, available seasons is somewhat of a deadend
    


    # Searching for a player using the players.get_players is nice if
    # you're looking for the player's id and if their active
    # otherwise it doesn't give you any actual stats
    nba_players = players.get_players()
    print("\n\n Printing info for the goat:")
    goat = [player for player in nba_players if player['full_name'] == 'Michael Jordan'][0]
    print(goat)
    print("\n")
    print("Player name: ", goat['full_name'], "\nIs Active: ", goat['is_active'])
    print("\n\n")


    # Career stats for Lebron James
    career = playercareerstats.PlayerCareerStats(player_id=2544)
    d3 = career.get_dict()
    

    
    # This prints all data for a player seperated by:
    # [0] -- SeasonTotalsRegularSeason
    # [1] -- CareerTotalsRegularSeason
    # [2] -- SeasonTotalPostSeason
    # [3] -- CareerTotalsPostSeason
    # [4] -- CareerTotalsAllStarSeasons
    # [5] -- SeasonTotalsCollegeSeasons -- NOT RELEVANT
    # [6] -- CareerTotalsCollegeSeason -- NOT RELEVANT
    # [7] -- SeasonRankingsRegularSeason -- EX. Lebron was #1 in PTS in 2007-08
    # [8] -- SeasonRankingPostSeasons 
    print("This is a dict of the entirety of the career stats of Lebron: ")
    print(d3['resultSets'], "\n\n")   

    # This gets a dict of the careertotalRegularstats
    print("This is a list of the careertotalRegularstats of Lebron: ")
    print(d3['resultSets'][1], "\n\n")
    
    # Just the headers for the PostSeason
    # Headers info includes:
    #
    # [0] -- PLAYER_ID
    # [1] -- SEASON_ID -- REFERS TO SPECIFIC SEASON FORMAT EX. '2007-08'
    # [2] -- LEAGUE_ID -- NOT COMPLETELY SURE WHAT THIS DOES
    # [3] -- TEAM_ID
    # [4] -- TEAM_ABBREVIATION
    # [5] -- PLAYER_AGE
    # [6] -- GP -- GAMES PLAYED
    # [7] -- GS -- GAMES STARTED
    # [8] -- MIN -- MINUTES PER SEASON
    # [9] -- FGM -- FIELD GOALS MADE
    # [10] -- FGA -- FIELD GOALS ATTEMPTED
    # [11] -- FG_PCT -- FIELD GOAL PERCENTAGE
    # [12] -- FG3M -- FIELD GOAL 3S MADE
    # [13] -- FG3A -- FIELD GOAL 3S ATTEMPTED
    # [14] -- FG3_PCT -- FIELD GOAL 3S PERCENTAGE
    # [15] -- FTM -- FREE THROWS MADE
    # [16] -- FTA -- FREE THROWS ATTEMPTED
    # [17 -- FT_PCT -- FREE THROW PERCENTAGE
    # [18] -- OREB -- OFFENSIVE REBOUNDS
    # [19] -- DREB -- DEFENSIVE REBOUNDS
    # [20] -- REB -- TOTAL REBOUNDS
    # [21] -- AST -- ASSISTS
    # [22] -- STL -- STEALS
    # [23] -- BLK -- BLOCKS
    # [24] -- TOV -- TURNOVERS
    # [25] -- PF -- PERSONAL FOULS
    # [26] -- PTS -- POINTS
    print("headers format: ")
    print(d3['resultSets'][2]['headers'], "\n\n")


    # Printing RowSet, who's format follows the headers format
    # This will print all post seasons Lebron played in
    print("This is a list of all seasons that Lebron played in: ")
    print(d3['resultSets'][2]['rowSet'])


if __name__ == '__main__':
    main()
