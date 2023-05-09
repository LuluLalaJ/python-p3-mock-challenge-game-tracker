class Result:


    all = []

    def __init__(self, player, game, score):
        from classes.player import Player
        from classes.game import Game
        if not isinstance(player, Player) or not isinstance(game, Game):
            raise Exception("""
            The player must be an instance of Player Class
            and the game must be an instance of Game Class!
            """)

        if not (1 <= score <= 5000):
            raise Exception("The score must be 1 and 5000, inclusive")

        self.player = player
        self.game = game
        self._score = score
        #what is the self below referring to?
        #the result instance
        player.results(self)
        player.games_played(game)
        game.results(self)
        game.players(player)
        self.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if 1 <= val <= 5000:
            self.score = val
        else:
            raise Exception("The score must be 1 and 5000, inclusive")
