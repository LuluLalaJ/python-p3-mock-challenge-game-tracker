class Game:
    def __init__(self, title):
        if isinstance(title, str) and 0 < len(title):
            self._title = title
        else:
            raise Exception('Titles must be strings greater than 0 characters')

        self._results = []
        self._players = []


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        raise Exception('Title cannot be changed after the Game is initialized')

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        # else:
        #     raise Exception
        return self._results

    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        # else:
        #     raise Exception
        return self._players

    def average_score(self, player):
        all_results = self._results
        player_results = [result for result in all_results if result.player == player]
        player_scores = [result.score for result in player_results]
        if player_scores:
            return sum(player_scores)/len(player_scores)
        else:
            return None 
