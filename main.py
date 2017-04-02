import state
import sys
import random
import history

BOARD_SIZE = 40 #Každých 10 políčok začína nový hráč (0, 10, 20, 30) 

game_state = None #mutovatelna premenna ukazujúca na aktuálny stav hry
num_of_players = 0

def start():
    global game_state
    global num_of_players
    while(num_of_players < 2 or num_of_players > 4):
        print("Zadajte pocet hracov (min. 2, max 4):")
        num_of_players = int(input())
    board = {}
    for i in range(0, num_of_players):
        board[i] = ("-1", "-1", "-1", "-1")
    game_state = state.State(num_of_players,board,random.randint(0, num_of_players-1)))
    play()

def get_command():    
    sys.stdout.write('$ ')
    sys.stdout.flush()
    return input()

def play():
    global game_state
    while(True):
        print('Na rade je hráč s číslom ' + str(game_state.get_next_player()))
        com = get_command()
        if(com == 'quit'):
            exit()
        elif(com == 'undo'):
            game_state = history.undo()
        elif(com == 'throw'):
            pass
        else:
            print('Neplatný príkaz. Možné príkazy sú: "throw", "undo" a "quit"')
            
start()
