import copy
import constants

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

team1 = {'team_name': 1, 'players': []}
team2 = {'team_name': 2, 'players': []}
team3 = {'team_name': 3, 'players': []}

team_list = [team1, team2, team3]


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

def display_stats(a):
    team_players = []
    experienced_players = []
    inexperienced_players = []
    names = []
    guardian_list = []
    heights = []

    def player_names():
        player_number = len(team_players)
        print("Total no. of players: {} \n".format(player_number))
        for player in team_players:
            names.append(player['name'])
        name_list = ', '.join(str(name) for name in names)
        print("Player names: {} \n".format(name_list))
            # print names of players (joined together as comma-seperated string, not a list)


    def average():
        for player in team_players:
            heights.append(player['height_2'])
        average = (sum(heights)/len(heights))
        print("Average height: {} \n".format(average))

    def exp_inexp():
        for player in team_players:
            if player['experience'] == True:
                experienced_players.append(player)
            else:
                inexperienced_players.append(player)
        print("No. of experienced players: {} \n".format(len(experienced_players)))
        print("No. of inexperienced players: {} \n".format(len(inexperienced_players)))
    
    def guardians():
        for player in team_players:
            for guardian in player['guardians']:
                guardian_list.append(guardian)
        guardianss = ', '.join(str(guardian) for guardian in guardian_list)
        print("Total no. of guardians: ", (len(guardian_list)), "\n")
        print("Guardian names: ", guardianss, "\n")

    if a == 1:
        team_players = team1['players']
    elif a == 2:
        team_players = team2['players']
    elif a == 3:
        team_players = team3['players']

    player_names()
    average()
    exp_inexp()
    guardians()

            
if __name__ == "__main__":

    clean_data()
    balance_team()

    print("Welcome to the Basketball Stats Tool. \n")
    while True:
        try:
            print("What would you like to do? \n\n 1. Display Team Stats \n 2. Quit \n")
            action_choice = int(input("Enter either 1 or 2: "))
            if action_choice == 1:
                print("-"*200)
                print(
                    "Which team's stats would you like? \n\n 1. Panthers \n 2. Bandits \n 3. Warriors \n")
                while True:
                    try:
                        n = int(input("Enter 1, 2 or 3: "))

                        if n == 1:
                            print("-"*200)
                            print(team1['team_name'], "\n")
                            display_stats(1)
                            print("-"*200)
                            break

                        elif n == 2:
                            print("-"*100)
                            print(team2['team_name'], "\n")
                            display_stats(2)
                            print("-"*200)
                            break

                        elif n == 3:
                            print("-"*100)
                            print(team3['team_name'], "\n")
                            display_stats(3)
                            print("-"*200)
                            break

                    except ValueError:
                        print("You have entered an invalid option. Please try again. ")

            if action_choice == 2:
                quit()

        except ValueError:
            print("You have entered an invalid option.")

# add functions that you do not want it to run on other files that import applications.py
