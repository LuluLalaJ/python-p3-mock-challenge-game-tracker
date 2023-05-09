class Player:

    all = []

    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise Exception("Username must be a string and between 2 and 16 characters")
        self._username = username
        self._results = []
        self._games_played = []
        self.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        if isinstance(val, str) and (2 <= len(val) <= 16):
            self._username = val
        else:
            raise Exception("Username must be a string and between 2 and 16 characters")

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        return self in game.players()

    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            maxscore = 0
            maxplayer = None
            for player in cls.all:
                if game.average_score(player) > maxscore:
                    maxscore = game.average_score(player)
                    maxplayer = player
            return maxplayer
        return None 
