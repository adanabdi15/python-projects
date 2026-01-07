#!/usr/bin/env python3

class Game:
    def __init__(self, date, home_team, opponent, home_score, opponent_score):
        self.__date = date
        self.__home_team = home_team
        self.__opponent = opponent
        self.__home_score = home_score
        self.__opponent_score = opponent_score

    def get_date(self):
        return self.__date

    def get_home_team(self):
        return self.__home_team

    def get_home_score(self):
        return self.__home_score

    def get_opponent(self):
        return self.__opponent

    def get_opponent_score(self):
        return self.__opponent_score

    def __str__(self):
        return (
            str(self.__date) + ": " +
            str(self.__home_team) + " " + str(self.__home_score) + ", " +
            str(self.__opponent) + " " + str(self.__opponent_score)
        )

    def winner(self):
        if self.__home_score > self.__opponent_score:
            return self.__home_team
        elif self.__opponent_score > self.__home_score:
            return self.__opponent
        else:
            return "Tie"


class Baseball_Game(Game):
    def __init__(self, date, home_team, opponent, home_score, opponent_score, winning_pitcher):
        super().__init__(date, home_team, opponent, home_score, opponent_score)
        self.__winning_pitcher = winning_pitcher

    def get_winning_pitcher(self):
        return self.__winning_pitcher

    def __str__(self):
        return super().__str__() + ", Winning pitcher: " + str(self.__winning_pitcher)


game_1 = Game("2007-10-24", "Red Sox", "Rockies", 13, 1)
print(game_1)
print(game_1.get_date())
print(game_1.get_home_team())
print(game_1.get_home_score())
print(game_1.get_opponent())
print(game_1.get_opponent_score())
print(game_1.winner())

game_2 = Baseball_Game("2007-10-24", "Red Sox", "Rockies", 13, 1, "Josh Beckett" )
print(game_2)
print(game_2.get_winning_pitcher())
