import state
import sys
import random
import history
import constants as con

game_state = None #mutovatelna premenna ukazujúca na aktuálny stav hry
game_history = None #bude sa odkazovať na inštanciu triedy History

def start():
    """
    Funkcia pripravujúca hru.
    Tu sa zisťuje počet hráčov a pripravuje sa prvý stav hry, kedy
    majú všetci hráči svoje figúrky v domčeku (sú na pozícií -1).
    """
    global game_state
    global game_history

    num_of_players = 0
    while(num_of_players < 2 or num_of_players > con.MAX_PLAYERS):
        print("Zadajte pocet hracov (min. 2, max " + str(con.MAX_PLAYERS) + "):")
        num_of_players = int(input())

    board = {}
    for i in range(0, num_of_players):
        board[i] = (-1, -1, -1, -1)
    
    game_state = state.State(num_of_players,board,random.randint(0, num_of_players-1))
    game_history = history.History()
    play()


def get_command():    
    """
    Jednoduchá deokária terminálu pridávajúca '$' pred užívateľov vstup.
    :returns: užívateľov vstup
    """
    sys.stdout.write('$ ')
    sys.stdout.flush()
    return input()

def print_state():
    """
    Vypísanie aktuálneho stavu hry na štandardný vžstup.
    """
    board = game_state.get_board()
    for key in board:
        sys.stdout.write('Hráč ' + str(key) + ' s figúrkami na pozíciach: ')
        for i in range(0, len(board[key])):
            sys.stdout.write(str(i) + ':' + str(board[key][i]) + ' ')

        sys.stdout.write(' Bodov: ' + str(game_state.get_score()[key]) + '\n')
    sys.stdout.write('Na rade je hráč s číslom '+str(game_state.get_next_player())+'\n')
    sys.stdout.flush()

def play():
    """
    Hranie hry. Funcia spracováva užívatelove príkazy
    a vykonáva ich. Predpoklad pre spustenie funkcie play
    je existencia stavu hry na ktorý ukazuje game_state.
    """
    global game_state
    while(True):
        print_state()
        com = get_command()

        if(com == 'quit'):
            print("Výsledné skóre:")
            res = []
            for i in range(0, len(game_state.get_score())):
                res.append((game_state.get_score()[i], i))
            for i in sorted(res, key = lambda x: x[0], reverse = True):
                print('Hráč ' + str(i[1]) + ' získal ' + str(i[0]) + ' bodov.')
            exit()
        elif(com == 'undo'):
            game_state = game_history.undo(game_state)
        elif(com == 'throw'):
            dice = random.randint(1, 6)
            piece = -1

            while(piece < 0 or piece > 3):
                print('Na kocke padlo číslo '+str(dice)+' vyberte figúrku pre ťah (0-3)')
                piece = int(input())
            game_state = game_history.execute(game_state, dice, piece)
        else:
            print('\nNeplatný príkaz. Možné príkazy sú: "throw", "undo" a "quit"\n')
            
start()
