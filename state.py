import copy

class State:
    
    """
    Trieda predstavujúca stav hry.
    board, herná plocha, je slovník tuplí, pre každého hráča jedna tupla
    v ktorej sa nachádzajú 4 prvky - pozície hráčových figúrok.
    num_of_players, počet hráčov v aktuálnej hre.
    next_player, hráč ktorý je aktuálne na ťahu, resp. ide hádzať kockou.
    score, tupla, ukladajúca si skóre jedntolivých hráčov (indexy sú čísla hráčov)
    vytvorí sa pri inicializácií objektu obsahujúca len nuly.
    """

    board = {}
    def __init__(self, num_of_players, board, next_player):
        self.num_of_players = num_of_players
        for key in board:
            self.board[key] = board[key] #očakávaná je tuple, ktorá je immutable
        self.next_player = next_player
        temp = []
        for i in range(0, num_of_players):
            temp.append(0)
        self.score = tuple(temp)

    def get_num_of_players(self):
        return self.num_of_players

    def get_next_player(self):
        return self.next_player

    def get_board(self):
        return copy.copy(self.board)

    def get_score(self):
        return self.score
