from __future__ import print_function 
from IPython.display import clear_output
import random

class TicTacToe:

    board = [" "] * 10
    player = 0

    def display_board(self):
        for i in range(9):
            print(" %s "%(str(self.board[i])),end="")
            if(i in [2,5,8]):
                print()
                continue
            print("|",end="")
    
    def place_marker(self, marker, position):
        position = int(position)
        self.board[position] = marker
        return self.board
    
    def space_check(self, position):
        if(self.board[position] == " "):
            return True
        else:
            return False
    
    def is_inboard(self, position):
     return position in [0,1,2,3,4,5,6,7,8]

    def rand_first(self):
        return random.randint(0,1)
    
    def boardfull_check(self):
        if(" " not in self.board):
            print("Draw")
            return True
    
    def win_check(self, marker):
        if(marker==self.board[0]==self.board[4]==self.board[8]) or \
            (marker==self.board[2]==self.board[4]==self.board[6]) or \
            (marker==self.board[0]==self.board[3]==self.board[6]) or \
            (marker==self.board[2]==self.board[5]==self.board[8]) or \
            (marker==self.board[1]==self.board[4]==self.board[7]) or \
            (marker==self.board[0]==self.board[1]==self.board[2]) or \
            (marker==self.board[3]==self.board[4]==self.board[5]) or \
            (marker==self.board[6]==self.board[7]==self.board[8]):
            print("player",self.player,"win")
            return True
            
        else:
            return False
    
    def reply(self):
        while(True):
            in_playagain = input("Do u wanna play again?[Y/N]")
            if(in_playagain in ['Y','y','yes','YES','Yes']):
                return True
            elif(in_playagain in ['N','n','no','NO','No']):
                return False
            else:
                print('invalid input')
    
    def player_input(self):
        while(True):
            try:
                number = int(input("player"+str(self.player)+" Enter ur position:"))
            except:
                print("You must enter a number")
            else:
                return number
    
    def playgame(self):
        self.board = [" "] * 10

        player_marker = {0:"O", 1:"X"}
        print("player0's marker is O \nplayer1's marker is X")

        self.player = self.rand_first()
        print("First player is player",self.player,sep="")

        self.display_board()

        while(True):#in-game loop
            while(True):   #marking loop

                position = self.player_input() - 1

                if(self.is_inboard(position) and self.space_check(position)):
                    self.board = self.place_marker(player_marker[self.player],position)
                    break
                else:
                    print("invalid value")
                    continue

            clear_output()
            self.display_board(self.board)

            if self.win_check(player_marker[self.player]) or self.boardfull_check():
                if self.reply():
                    clear_output()
                    self.playgame()
                    
                else:
                    print("Game end")
                    return
                    

            self.player = (self.player+1)%2  


tictactoe = TicTacToe()
tictactoe.playgame()