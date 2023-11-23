class ScorePrinter:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name

    def display_ongoing_score(self, player_one_score, player_two_score):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score = score_names[player_one_score]

        is_tie = player_two_score == player_one_score

        if is_tie:
            return score + "-All"
        else:
            return score + "-" + score_names[player_two_score]

    def display_endgame_score(self, player_one_score, player_two_score):

        is_tie = player_one_score == player_two_score
        if is_tie:
            return "Deuce"

        is_advantage_stage = ((player_one_score - player_two_score) * (
                player_one_score - player_two_score) == 1)

        if is_advantage_stage:
            return "Advantage " + self.__get_winning_player(player_one_score,player_two_score)
        else:
            return "Win for " + self.__get_winning_player(player_one_score,player_two_score)

    def __get_winning_player(self, player_one_score, player_two_score):
        return self.__player_one_name if player_one_score > player_two_score else self.__player_two_name
