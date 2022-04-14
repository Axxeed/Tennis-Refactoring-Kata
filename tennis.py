# -*- coding: utf-8 -*-


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)

    def won_point(self, playerName):
        if self.score().startswith("Win for"):
            raise Exception("Game is over")
        if playerName == self.player1.name:
            self.player1.points += 1
        elif playerName == self.player2.name:
            self.player2.points += 1
        else:
            raise Exception(playerName + " is not playing")

    def score(self):
        if (self.player1.points < 4 and self.player2.points < 4) and (
            self.player1.points + self.player2.points < 6
        ):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            p = points[self.player1.points]
            return (
                p + "-All"
                if (self.player1.points == self.player2.points)
                else p + "-" + points[self.player2.points]
            )
        else:
            if self.player1.points == self.player2.points:
                return "Deuce"
            s = (
                self.player1.name
                if self.player1.points > self.player2.points
                else self.player2.name
            )
            return (
                "Advantage " + s
                if (
                    (self.player1.points - self.player2.points)
                    * (self.player1.points - self.player2.points)
                    == 1
                )
                else "Win for " + s
            )
