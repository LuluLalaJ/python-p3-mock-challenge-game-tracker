class Player:

    all = []

    def __init__(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Usernames must be strings between 2 and 16 characters, inclusive.')
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Usernames must be strings between 2 and 16 characters, inclusive.')

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        # else:
        #     raise Exception
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        # else:
        #     raise Exception
        return self._games_played

    def played_game(self, game):
        return self in game.players()

    def num_times_played(self, game):
        results = game.results()
        return len([result for result in results if result.player == self])

    @classmethod
    def highest_scored(cls, game):
        players = game.players()
        if players:
            highest = 0
            highest_player = None
            for player in players:
                if game.average_score(player) > highest:
                    highest = game.average_score(player)
                    highest_player = player
            return highest_player
        return None
