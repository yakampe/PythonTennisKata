class ScoreCounter:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name
        self.__player_one_score = 0
        self.__player_two_score = 0

    def increase_score(self, scoring_player):
        if scoring_player == self.__player_one_name:
            self.__player_one_scored()
        else:
            self.__player_two_scored()

    def __player_one_scored(self):
        self.__player_one_score += 1

    def __player_two_scored(self):
        self.__player_two_score += 1

    def get_player_one_score(self):
        return self.__player_one_score

    def get_player_two_score(self):
        return self.__player_two_score
