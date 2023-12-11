from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or


def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.playsIn("NYR").hasAtLeast(
        10, "goals").hasFewerThan(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)


class QueryBuilder:
    def __init__(self, query=All([])):
        self._query = query

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def build(self):
        return self._query


if __name__ == "__main__":
    main()
