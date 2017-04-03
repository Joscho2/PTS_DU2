import state
import copy
import constants as con

class History:
    
    state_history = []
        
    def edit_tuple(self, board, key, new, index):
        """
        Vytvorí novú tuplu s hodnotou new na pozícií index a položí na miesto starej
        vo vstupnom slovníku board.
        """
        temp_list = list(board[key])
        temp_list[index] = new
        board[key] = tuple(temp_list)
    def execute(self, g_state, move, piece):
        new_state = copy.copy(g_state)
        self.state_history.append(copy.copy(g_state))

        n_players = g_state.get_num_of_players()
        player = g_state.get_next_player()
        next_player = player if move == 6 else (player + 1) % n_players               
        new_state.next_player = next_player
        board = new_state.get_board()
        
        position = board[player][piece]
        if(position == -1):
            #ak hodí 1 začína na svojom "štarte", od toho čo padlo na kocke odčítame -1
            position += player*con.OFFSET + move
        else:
            if ((position < player*con.OFFSET and position + move >= player*con.OFFSET)
            or (position + move >= con.BOARD_SIZE
            and (position + move) % con.BOARD_SIZE >= player*con.OFFSET)):
                print("Hráč " + str(player) + " získava 1 bod!")
                temp = list(new_state.get_score())
                temp[player] += 1
                new_state.score = tuple(temp) 
            position += move
            position %= con.BOARD_SIZE
        position = int(position)

        for key in board:
            #je možné mať viac vlastných figúrok na rovnakej pozicií
            if(key == player): continue            
            tpl = board[key]
            for i in range(0, len(tpl)):
                if(tpl[i] == position):
                    self.edit_tuple(board, key, -1, i)
                    break
        self.edit_tuple(board, player, position, piece)
        new_state.board = board
        return new_state
    def undo(self, actual_state):
        if(len(self.state_history) > 0):
            res = self.state_history.pop()
            #print(str(self.state_history[len(self.state_history) -1].get_board()))
            return res
        else:
            print('Nie je možné vykonať krok späť, ste na začiatku hry!')
            return actual_state
