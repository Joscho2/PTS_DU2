class State:
    def __init__(self, num_of_players, board ):
        self.num_of_players = num_of_players
        for i in board:
             for key in i:
                 self.board[key] = i[key]
        
