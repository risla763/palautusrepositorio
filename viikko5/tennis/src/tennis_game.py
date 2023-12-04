class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""
        temp_score = 0
        player_score_list = ["Love-All", "Fifteen-All", "Thirty-All"]
        advatages_wins_list = [
            "Advantage player1", "Advantage player2", "Win for player1", "Win for player2"]
        scores = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                score = player_score_list[0]
            elif self.player1_score == 1:
                score = player_score_list[1]
            elif self.player1_score == 2:
                score = player_score_list[2]
            else:
                score = "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score

            if minus_result == 1:
                score = advatages_wins_list[1]
            elif minus_result == -1:
                score = advatages_wins_list[2]
            elif minus_result >= 2:
                score = advatages_wins_list[3]
            else:
                score = advatages_wins_list[4]
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + scores[0]
                elif temp_score == 1:
                    score = score + scores[1]
                elif temp_score == 2:
                    score = score + scores[2]
                elif temp_score == 3:
                    score = score + scores[3]

        return score
