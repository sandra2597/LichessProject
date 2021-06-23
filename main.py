from methods import *

# Path to the csv file containing the selected games. This csv file is created by the program Sevilla from JBF software
path_to_csv_file = 'Games.csv'

# Path to the json file which contains the necessary authorization tokens for lichess.org
path_to_token_data = "auth_tokens.json"

# time limit in seconds
clock_limit = 300

# time increment in seconds
clock_increment = 0

games = import_games(path_to_csv_file)
created_game_ids = []
for game in games:
    response = create_challenge(game[0], game[1], clock_limit,
                                clock_increment, path_to_token_data)
    if response.status_code == 200:
        created_game_ids.append(response.json()['challenge']['id'])

# writing game id data to two seperate files.
# The file 'game_iframes.txt' contains all the iframes which can directly be pasted in the html of a webpage.
# The file 'game_ids.txt' consists just of the game ids, this is used to fetch the game results.
with open('game_iframes.txt', 'w') as fp:
    for id in created_game_ids:
        fp.write(f'''<iframe src="https://lichess.org/embed/{id}?theme=auto&bg=auto"
width=600 height=397 frameborder=0></iframe>''')
with open('game_ids.txt', 'w') as fp:
    for id in created_game_ids:
        fp.write(id)
