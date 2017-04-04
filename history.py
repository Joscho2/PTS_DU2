import state
import copy
import constants as con

class History:

    """
    Trieda starajúca sa o vykonávanie zmien v hre, o zmenu herných stavov
    a o ukladanie si ešte nezmenených stavov v pamäti, vďaka čomu sa bude dať
    pohodlne vrátiť k akémukoľvek predchádzajúcemu hernému stavu.
    """
    
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
        """
        Metóda vykonávajúca všetky zmeny v hre.
        Aktuálny stav si uloží do histórie, skopíruje si ho, ten pozmení a vracia.
        Parametre:
        g_state --aktuálny resp. predchádzajúci stav hry, ktorý je uložený do hstórie
        move --číslo aké padlo na kocke, o koľko sa má figúrka hráča posunúť
        piece --číslo figúrky daného hráča (vždy je to číslo medzi 0 - 3 vrátane)
        """
        new_state = copy.copy(g_state)
        self.state_history.append(copy.copy(g_state))
        
        #Výpočet nasledujúceho hráča, ak padla na kocke 6, hráč sa nemení
        n_players = g_state.get_num_of_players()
        player = g_state.get_next_player()
        next_player = player if move == 6 else (player + 1) % n_players               
        new_state.next_player = next_player
        board = new_state.get_board()
        
        #Posun figúrky a pripočítavanie bodov. Ak hráč nejakou figúrkou
        #prejde cez svoje štartovacie políčko, získa 1 bod
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
        
        #Vyhadzovanie súperových figúrok
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
        """
        Podľa histórie vracanie posledného stavu hry.
        Paramater actual_state má byť aktuálny stav hry, ktorý
        bude vrátený v prípade, že je sa v histórií už nič nenachádza.
        """
        if(len(self.state_history) > 0):
            res = self.state_history.pop()
            #print(str(self.state_history[len(self.state_history) -1].get_board()))
            return res
        else:
            print('Nie je možné vykonať krok späť, ste na začiatku hry!')
            return actual_state
