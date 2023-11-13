import requests
from player import Player
import PlayerReader
from PlayerStats import Stats


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = Stats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

def main():
    pass

if __name__ == "__main__":
    main()
