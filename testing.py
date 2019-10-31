from tkinter import *
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
#from nba_api.stats.static import teams
#nba_teams = teams.get_teams()
#dict_nba_team=one_dict(nba_teams)
#df_teams=pd.DataFrame(dict_nba_team)

root = Tk()
root.geometry("500x500")

topFrame = Frame(root)
entry = Entry(topFrame)
entry.pack()

def clicked():
    T.delete('1.0', END)
    T.update()
    player = entry.get()
    print(player)
    player_list_full_name = players.find_players_by_full_name(player)
    player_list_first_name = players.find_players_by_first_name(player)
    player_list_last_name = players.find_players_by_last_name(player)
    complete_list = player_list_full_name + player_list_first_name
    complete_list += player_list_last_name
    res = [] 
    for i in complete_list:
        if i not in res: 
           res.append(i)
    #print(type(res))
    #list1 = '\n'.join(map(str, player_list_first_name))
    #T.insert(INSERT, list1)
    #T.insert(INSERT, player_list_full_name)
    s = ""
    print(len(res))
    for i in range(0, len(res)):
        id1 = res[i]['id']
        player1 = commonplayerinfo.CommonPlayerInfo(player_id=id1)
        d = player1.get_normalized_dict()
        s += res[i]['full_name'] + ' #'
        s += d['CommonPlayerInfo'][0]['JERSEY'] + '\n'
        s += d['CommonPlayerInfo'][0]['TEAM_CITY'] + ' '
        s += d['CommonPlayerInfo'][0]['TEAM_NAME'] + '\n'
        s += "Height: " + d['CommonPlayerInfo'][0]['HEIGHT'] + ' '
        s += "Weight: " + d['CommonPlayerInfo'][0]['WEIGHT'] + '\n'
        s += "College: " + d['CommonPlayerInfo'][0]['SCHOOL'] + '\n\n'
    T.insert(INSERT, s)
    

button = Button(topFrame, text="search", command = clicked)
button.pack()

topFrame.pack(side = TOP)

bottomFrame = Frame(root)
T = Text(bottomFrame, height=25, width=70, bg = "yellow")
T.pack()
bottomFrame.pack(side=BOTTOM)

#root.mainLoop()
