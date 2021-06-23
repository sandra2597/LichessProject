import requests

# prints out the white player, the black player and the status of the game given a certain game id on lichess.org


def fetch_game(gameId):
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    response = requests.get(
        f'https://lichess.org/game/export/{gameId}', headers=headers)
    if response.status_code == 200:
        data = response.json()
        white = data['players']['white']['user']['id']
        black = data['players']['black']['user']['id']
        if 'winner' in data:
            if data['winner'] == 'white':
                status = '1-0'
            else:
                status = '0-1'
        else:
            status = data['status']
            if status == 'draw':
                status = '1/2-1/2'
        return f'{white}-{black}     {status}'
    else:
        return f'game {gameId} not found'


# read game data from game_ids.txt
with open('game_ids.txt', 'r') as fp:
    for line in fp.readlines():
        line = line.replace('\n', '')
        if line != '':
            print(fetch_game(line))
