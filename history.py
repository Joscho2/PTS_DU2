import state

class History:
    
    state_history = []
    board_size = 0

    def __init__(board_size):
        self.board_size = board_size
    def execute(state, move_count, piece):
        state_history.append(state)

        player = state.get_next_player()
        posistion = state.get_board()[player][piece]
        if(position == -1):
            position += player*10 + move_count
        else:
            position += move_count
        
        board = state.get_board()
        for key in board:
            if(key == player): continue
            tpl = board[key]
            for i in range(0, len(tpl)):
                if(tpl[i] == position):
                    temp_list = list(tpl)
                    temp_list[i] = -1
                    board[key] = tuple(temp_list)
                    break
        board[player]
        n_players = state.get_num_of_players()
        next_player = (player + 1) % n_players
        res_state = state.State(n_players, board, next_player)
        return res_state
