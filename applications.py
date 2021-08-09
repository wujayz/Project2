if __name__ == "__main__":
    print(__name__)
    # later add this if-statement at the end/bottom of the file
    # add functions that you do not want it to run on other files that import app.py

import copy
import constants

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

def clean_data():
    experienced_players = []
    inexperienced_players = []
    for player in players:
        height_int = int(player['height'][0:2])
        player['height_2'] = height_int

        player['guardians'] = player['guardians'].split(' and ')
        
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

def balance_team():
    player_per_team = int(len(players)/len(teams))

    team1 = {'team_name': 1, 'players': []}
    team2 = {'team_name': 2, 'players': []}
    team3 = {'team_name': 3, 'players': []}

    team_list = [team1, team2, team3]
    
    n = 0
    for team in team_list:
        team['team_name'] = teams[n]
        n += 1

        for player in players[:]:
            if player['experience'] == True:
                team['players'].append(player)
                players.remove(player)
            
            if len(team['players']) == int(player_per_team/2):
                break

        for player in players[:]:
            if player['experience'] == False:
                team['players'].append(player)
                players.remove(player)
        
            if len(team['players']) == player_per_team:
                break
    
            

clean_data()
balance_team()
