# -*- coding: utf-8 -*-

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


class TennisGame3Solid:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name
        self.__score_counter = ScoreCounter()

    def won_point(self, scoring_player):
        if scoring_player == self.__player_one_name:
            self.__score_counter.player_one_scored()
        else:
            self.__score_counter.player_two_scored()

    def score(self):
        if self.__score_counter.is_endgame():
            return self.__return_endgame_score()
        else:
            return self.__return_ongoing_score()



    def __return_ongoing_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        score = score_names[self.__score_counter.player_one_score()]

        is_tie = self.__score_counter.player_two_score() == self.__score_counter.player_one_score()

        if is_tie:
            return score + "-All"
        else:
            return score + "-" + score_names[self.__score_counter.player_two_score()]

    def __return_endgame_score(self):
        is_tie = self.__score_counter.player_one_score() == self.__score_counter.player_two_score()
        if is_tie:
            return "Deuce"

        is_advantage_stage = ((self.__score_counter.player_one_score() - self.__score_counter.player_two_score()) * (
                self.__score_counter.player_one_score() - self.__score_counter.player_two_score()) == 1)

        if is_advantage_stage:
            return "Advantage " + self.__get_winning_player()
        else:
            return "Win for " + self.__get_winning_player()

    def __get_winning_player(self):
        return self.__player_one_name if self.__score_counter.player_one_score() > self.__score_counter.player_two_score() else self.__player_two_name
