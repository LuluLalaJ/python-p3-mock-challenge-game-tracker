class Game:
    def __init__(self, title):
        if not (isinstance(title, str)) or len(title) <= 0:
            raise Exception("Game title must be a string with length longer than 0")
        self._title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        raise Exception("Game title cannot be changed after the Game is initialized.")

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players

    def average_score(self, player):
        #zerodivision!!!
        scores = [result.score for result in self._results if result.player == player]
        if scores:
            return sum(scores)/len(scores)
        return 0
