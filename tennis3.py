# -*- coding: utf-8 -*-

class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.__player_one_name = player1Name
        self.__player_two_name = player2Name
        self.__player_one_score = 0
        self.__player_two_score = 0

    def won_point(self, players_who_won):
        if players_who_won == self.__player_one_name:
            self.__player_one_score += 1
        else:
            self.__player_two_score += 1

    def score(self):
        is_early_game = (self.__player_one_score < 4 and self.__player_two_score < 4) and (
                self.__player_one_score + self.__player_two_score < 6)

        if is_early_game:
            return self.__get_early_game_score()
        else:
            return self.__get_end_game_score()

    def __get_end_game_score(self):
        same_score = self.__player_one_score == self.__player_two_score
        if same_score:
            return "Deuce"
        winning_player = self.__get_winning_player()
        if (self.__player_one_score - self.__player_two_score) * (
                self.__player_one_score - self.__player_two_score) == 1:
            return "Advantage " + winning_player
        else:
            return "Win for " + winning_player

    def __get_early_game_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        same_score = self.__player_one_score == self.__player_two_score
        score = score_names[self.__player_one_score]
        if same_score:
            return score + "-All"
        else:
            return score + "-" + score_names[self.__player_two_score]

    def __get_winning_player(self):
        return self.__player_one_name if self.__player_one_score > self.__player_two_score else self.__player_two_name
