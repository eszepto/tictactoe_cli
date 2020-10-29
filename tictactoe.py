from __future__ import print_function 
from IPython.display import clear_output

def display_board():
    global board
    for i in range(9):
        print(" %s "%(str(board[i])),end="")
        if(i in [2,5,8]):
            print()
            continue
        print("|",end="")
        
def place_marker(marker,position):
    global board
    position = int(position)
    board[position] = marker
    return board

def space_check(position):
    global board
    if(board[position] == " "):
        return True
    else:
        return False
    
def is_inboard(position):
    return position in [0,1,2,3,4,5,6,7,8]

def rand_first():
    import random
    return random.randint(0,1)



def boardfull_check():
    global board
    if(" " not in board):
        print("Draw")
        return True


    
def win_check(marker):
    global board,player
    if(marker==board[0]==board[4]==board[8]) or \
        (marker==board[2]==board[4]==board[6]) or \
        (marker==board[0]==board[3]==board[6]) or \
        (marker==board[2]==board[5]==board[8]) or \
        (marker==board[1]==board[4]==board[7]) or \
        (marker==board[0]==board[1]==board[2]) or \
        (marker==board[3]==board[4]==board[5]) or \
        (marker==board[6]==board[7]==board[8]):
        print("player",player,"win")
        return True
        
    else:
        return False

def reply():
    while(True):
        in_playagain = input("Do u wanna play again?[Y/N]")
        if(in_playagain in ['Y','y','yes','YES','Yes']):
            return True
        elif(in_playagain in ['N','n','no','NO','No']):
            return False
        else:
            print('invalid input')
            
def player_input():
    while(True):
        try:
            number = int(input("player"+str(player)+" Enter ur position:"))
        except:
            print("You must enter a number")
        else:
            return number


board = [" "] * 10
player = 0
def playgame():
    global board
    global player
    board = [" "] * 10

    player_marker = {0:"O", 1:"X"}
    print("player0's marker is O \nplayer1's marker is X")

    player = rand_first()
    print("First player is player",player,sep="")

    display_board()

    while(True):#in-game loop
        while(True):   #marking loop

            position = player_input() - 1

            if(is_inboard(position) and space_check(position)):
                board = place_marker(player_marker[player],position)
                break
            else:
                print("invalid value")
                continue

        clear_output()
        display_board()

        if win_check(player_marker[player]) or boardfull_check():
            if reply():
                clear_output()
                playgame()
                
            else:
                print("Game end")
                return
                

        player = (player+1)%2  

playgame()