def start():
    num_of_players = 0
    while(num_of_players < 2 or num_of_players > 4):
        print("Zadajte pocet hracov (min. 2, max 4):")
        num_of_players = int(input())
    
start()
