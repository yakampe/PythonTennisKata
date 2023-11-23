# -*- coding: utf-8 -*-

class TennisGame3Solid:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name
        self.__player_one_score = 0
        self.__player_two_score = 0

    def won_point(self, scoring_player):
        if scoring_player == self.__player_one_name:
            self.__player_one_score += 1
        else:
            self.__player_two_score += 1

    def score(self):
        is_endgame = not ((self.__player_one_score < 4 and self.__player_two_score < 4) and (
                self.__player_one_score + self.__player_two_score < 6))
        if is_endgame:
            return self.__return_endgame_score()
        else:
            return self.__return_ongoing_score()

    def __return_ongoing_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score = score_names[self.__player_one_score]

        is_tie = self.__player_one_score == self.__player_two_score

        if is_tie:
            return score + "-All"
        else:
            return score + "-" + score_names[self.__player_two_score]

    def __return_endgame_score(self):
        is_tie = self.__player_one_score == self.__player_two_score
        if is_tie:
            return "Deuce"

        is_advantage_stage = ((self.__player_one_score - self.__player_two_score) * (
                self.__player_one_score - self.__player_two_score) == 1)

        if is_advantage_stage:
            return "Advantage " + self.__get_winning_player()
        else:
            return "Win for " + self.__get_winning_player()

    def __get_winning_player(self):
        return self.__player_one_name if self.__player_one_score > self.__player_two_score else self.__player_two_name
