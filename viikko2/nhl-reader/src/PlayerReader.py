import requests
from player import Player
class PlayerReader:
    def json(self, url):
        response = requests.get(url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

