if __name__ == "__main__":
    print(__name__)
    # later add this if-statement at the end/bottom of the file
    # add functions that you do not want it to run on other files that import app.py

import constants

def clean_data():
    experienced_players = []
    inexperienced_players = []
    for player in constants.PLAYERS:
        # height to integer
        height_int = int(player['height'][0:2])
        player['height_2'] = height_int
        
        # guardians
        player['guardians'] = player['guardians'].split(' and ')

        # experience
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        

#---------------------------------------------------------------------------------- works upto here

       
def balance_team():
    # find how many players to assign per team
    player_per_team = int(len(constants.PLAYERS)/len(constants.TEAMS))
    #make team dictionary of team name, team players, team stats
    # 1. make team dictionary

    team1 = {'team_name': 1, 'players':[]}
    team2 = {'team_name': 1, 'players': []}
    team3 = {'team_name': 1, 'players': []}
    # inside the dictionaries team1-3, 'players' is a key to value which is a list of (dictionaries per player)

    team_list = [team1, team2, team3]

    #adding team names for each team
    for team in team_list:
        n = 0
        team['team_name'] = constants.TEAMS[n]
        n += 1

#        # 2. assign players to teams
    for team in team_list:
        #while len(team['players']) <= (player_per_team/2):
            for players in constants.PLAYERS:
                if players['experience'] == True:
                    team['players'] += [players]
                    (constants.PLAYERS).remove(players)
                if len(team['players']) >= player_per_team/2:
                    break

    print(len(team1['players']))
    print(len(team2['players']))
    print(len(team3['players']))
    print(constants.PLAYERS)
    print(len(constants.PLAYERS))
            


#        while int(len(team['players'])) <= player_per_team:
clean_data()
balance_team()       
# ---------------------------------------------------------------------------------------
                    

    #team1 = {'team_name':1}
    #team2 = {'team_name':2}
    #team3 = {'team_name':3}
    #for team in constants.TEAMS:
    #    n = 0
    #    team_list[n]['team_name'] = team
    
    #print(team_list)




        







# 2. balance_team function: assign same no. of players per team; each team should have same no. of exp. / inexp. player per team, 


# 3. Menu: display stats of chosen team, or quit
