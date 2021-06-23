import csv
import json
import requests

# loads the csv file and returns an array with the games in the format [[white, black],[white,black],...]


def import_games(path_to_csv_file):
    games = []
    with open(path_to_csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rownumber = 0
        for row in reader:
            rownumber += 1
            if rownumber > 4 and row != []:
                # The break for Absences allows the program to stop reading if there are a odd number of players present.
                if 'Absences' in row:
                    break
                row = row[0].split(';=')
                white = row[1].replace('"', '')
                black = row[3].replace('"', '')
                games.append([white, black])
    return games

# Searches for the matching auhorization token for a player name


def get_token(name, path_to_token_data):
    with open(path_to_token_data) as json_file:
        tokens = json.load(json_file)
    if name in tokens:
        return tokens[name]
    else:
        print(f"token of {name} is not present in {path_to_token_data}")
        return None

# Sends post requests to lichess.org to create a game.


def create_challenge(white, black, clock_limit, clock_increment, path_to_token_data):
    auth_token_white = get_token(white, path_to_token_data)
    if auth_token_white is None:
        return 1
    auth_token_black = get_token(black, path_to_token_data)
    if auth_token_black is None:
        return 1
    headers = {'Authorization': f'Bearer {auth_token_white}'}
    params = {
        'color': 'white',
        'clock.limit': clock_limit,
        'clock.increment': clock_increment,
        'acceptByToken': auth_token_black
    }
    response = requests.post(
        f"https://lichess.org/api/challenge/{black}", headers=headers, data=params)
    if response.status_code == 200:
        print(f"Game {white}-{black} is created successfully")
    else:
        print(f"Could not create game: {white}-{black}. {response.json()}")
    return response
