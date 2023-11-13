import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()


    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from fin:")

    for player in players:
        if player.nationality == "FIN":
            print(player)

def main():
    pass

if __name__ == "__main__":
    main()
