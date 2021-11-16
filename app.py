import constants

all_players = []
teams = []


#Welcome information
def welcome():
    app_name = 'BASKETBALL TEAM STATS TOOL'
    print("*" * len(app_name))
    print(app_name)
    print("*" * len(app_name), end="\n\n\n")
    print("-" * 10, "MENU", "-" * 10, end="\n\n")

#Menu Options
def menu():
	continue_app = True
	menu_options = ['Display Team Stats', 'Quit']
	for index, item in enumerate(menu_options, start = 1):
		print("{}) {}".format(index, item))
	print('\nPlease enter your choice of option >\n')
	while continue_app == True:
		answer = input()
		if answer == '1':
			show_team_data()
		elif answer == '2':
			continue_app = False
			print ('See you next time')
	


#Clean player data
def clean_constants():
	for p in constants.PLAYERS:
		player_data = p
		player = {'Name': player_data['name'], 'Guardians': player_data['guardians']}
		if player_data['experience'] == 'YES':
			player['experience'] = True
		else:
			player['experience'] = False
		height_data = player_data['height'].split()
		player['height'] = int(height_data[0])
		global all_players
		all_players.append(player)
		


#balance the teams
def divide_players():
	num_players = len(all_players)
	players_per_team = num_players / 3
	team_index = 0
	for team in constants.TEAMS:
		first_player_index = team_index * players_per_team
		players = all_players[int(first_player_index): int((team_index + 1) * players_per_team)]
		team_stats = {'Team Name': team, 'Players': players}
		teams.append(team_stats)
		team_index += 1
	#print(teams)
	

# Display all team information
def show_team_data():
    divide_players()
    print('\nPlease select a team >\n')
    for index, item in enumerate(teams, start=1):
        print('{}) {}'.format(index, item['Team Name']))
    team_choice = input()
    team = teams[int(team_choice) - 1]
    print(f"\nTeam Name: {team['Team Name']}")
    print("*" * 20)
    print(f"\nTotal players: {len(team['Players'])}\n")
    players = team['Players']
    for player in players:
        print(f"\n{player['Name']}")

def main():
	print('application started')
	clean_constants()
	welcome()
	menu()
	

	#print (all_players)
	
if (__name__ == '__main__'):
	main()


