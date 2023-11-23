class ScoreCounter:
    def __init__(self):
        self.__player_one_score = 0
        self.__player_two_score = 0

    def player_one_scored(self):
        self.__player_one_score += 1

    def player_two_scored(self):
        self.__player_two_score += 1

    def is_endgame(self):
        return not ((self.__player_one_score < 4 and self.__player_two_score < 4) and (
                self.__player_one_score + self.__player_two_score < 6))

    def player_one_score(self):
        return self.__player_one_score

    def player_two_score(self):
        return self.__player_two_score
