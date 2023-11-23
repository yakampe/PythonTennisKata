# -*- coding: utf-8 -*-
from score_counter import ScoreCounter
from score_printer import ScorePrinter


class TennisGame3Solid:
    def __init__(self, player1Name, player2Name):
        self.__score_counter = ScoreCounter(player1Name, player2Name)
        self.__score_display = ScorePrinter(player1Name, player2Name)

    def won_point(self, scoring_player):
        self.__score_counter.increase_score(scoring_player)

    def score(self):
        return self.__score_display.display_score(self.__score_counter.get_player_one_score(),
                                                  self.__score_counter.get_player_two_score())
