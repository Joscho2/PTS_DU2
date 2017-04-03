import state
import sys
import random
import history

BOARD_SIZE = 40 #Každých 10 políčok začína nový hráč (0, 10, 20, 30) 

game_state = None #mutovatelna premenna ukazujúca na aktuálny stav hry
num_of_players = 0
game_history = None

def start():
    global game_state
    global num_of_players
    global game_history
    while(num_of_players < 2 or num_of_players > 4):
        print("Zadajte pocet hracov (min. 2, max 4):")
        num_of_players = int(input())
    board = {}
    for i in range(0, num_of_players):
        board[i] = (-1, -1, -1, -1)
    game_state = state.State(num_of_players,board,random.randint(0, num_of_players-1))
    game_history = history.History(BOARD_SIZE)
    play()

def get_command():    
    sys.stdout.write('$ ')
    sys.stdout.flush()
    return input()

def print_state():
    board = game_state.get_board()
    for key in board:
        sys.stdout.write('Hráč ' + str(key) + ' s figúrkami na pozíciach: ')
        for i in range(0, len(board[key])):
            sys.stdout.write(str(i) + ':' + str(board[key][i]) + ' ')
        sys.stdout.write('\n')
    sys.stdout.write('Na rade je hráč s číslom '+str(game_state.get_next_player())+'\n')
    sys.stdout.flush()

def play():
    global game_state
    while(True):
        print_state()
        com = get_command()
        if(com == 'quit'):
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
