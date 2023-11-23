# -*- coding: utf-8 -*-
from score_counter import ScoreCounter
from score_printer import ScorePrinter


class TennisGame3Solid:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name
        self.__score_counter = ScoreCounter()
        self.__score_display = ScorePrinter(player1Name, player2Name)

    def won_point(self, scoring_player):
        if scoring_player == self.__player_one_name:
            self.__score_counter.player_one_scored()
        else:
            self.__score_counter.player_two_scored()

    def score(self):
        return self.__score_display.display_score(self.__score_counter.get_player_one_score(),
                                                  self.__score_counter.get_player_two_score())
