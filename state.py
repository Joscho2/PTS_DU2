import copy

class State:
    
    board = {}
    def __init__(self, num_of_players, board, next_player):
        self.num_of_players = num_of_players
        for key in board:
            self.board[key] = board[key] #očakávaná je tuple, ktorá je immutable
        self.next_player = next_player
    def get_num_of_players(self):
        return self.num_of_players
    def get_next_player(self):
        return self.next_player
    def get_board(self):
        return copy.copy(self.board) #stačí shallow copy (to je čo copy.copy(obj) robí)
    
