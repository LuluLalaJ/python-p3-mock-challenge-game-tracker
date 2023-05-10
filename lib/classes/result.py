from classes.player import Player
from classes.game import Game
class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        # if (isinstance(player, Player)):
        #     self._player = player
        # else:
        #     raise Exception("the player is not an instance of Player class")

        # if (isinstance(game, Game)):
        #     self._game = game
        # else:
        #     raise Exception('the game is not an instance of Game class')

        self.score = score

    #why do we have to call them here?
        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)
        self.all.append(self)

    @property
    def player(self):
        return self._player


    @player.setter
    def player(self, player):
        if (isinstance(player, Player)):
            self._player = player
        else:
            raise Exception("the player is not an instance of Player class")


    @property
    def game(self):
        return self._game


    @game.setter
    def game(self, game):
        if (isinstance(game, Game)):
            self._game = game
        else:
            raise Exception('the game is not an instance of Game class')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("the score must be integers between 1 and 5000, inclusive")
