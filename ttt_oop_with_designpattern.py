import random


class Tictactoe():
    def __init__(self):
        self.board = Board()
        self.players = [Player("O"), Player("X")]
        self.outputter = Outputter()
        self.current_player = random.randint(0,1)

    def playgame(self):
        self.outputter.print("player0's marker is O \nplayer1's marker is X")

        print("First player is player", self.current_player + 1, sep="")

        self.outputter.display_board(self.board)

        while(True):#in-game loop
            while(True):   #marking loop

                position = self.outputter.player_input(self.current_player) - 1

                if(self.board.inboard_check(position) and self.board.available_check(position)):
                    self.board.place_marker(self.players[self.current_player], position)
                    break
                else:
                    print("invalid value")


            self.outputter.clear()
            self.outputter.display_board(self.board)

            if self.board.win_check(self.players[self.current_player]) or self.board.boardfull_check():
                if self.outputter.ask_playagain():
                    # clear_output()
                    self.playgame()
                    
                else:
                    print("Game end")
                    return
                    
            self.current_player = 1 if self.current_player == 0 else 0
class Board:
    def __init__(self, n):
        self.squares = [" "] * n
    def clear():
        self.squares = [" "] * len(self.squares)
        
class Board3x3(Board):
    BOARDSIZE = 9

    def __init__(self):
        super().__init_(BOARDSIZE)

class TictactoeBoard(Board3x3):
    
    def __init__(self):
        super().__init__()

    def win_check(self, player):
        marker = player.marker
        if(marker==self.squares[0]==self.squares[4]==self.squares[8]) or \
            (marker==self.squares[2]==self.squares[4]==self.squares[6]) or \
            (marker==self.squares[0]==self.squares[3]==self.squares[6]) or \
            (marker==self.squares[2]==self.squares[5]==self.squares[8]) or \
            (marker==self.squares[1]==self.squares[4]==self.squares[7]) or \
            (marker==self.squares[0]==self.squares[1]==self.squares[2]) or \
            (marker==self.squares[3]==self.squares[4]==self.squares[5]) or \
            (marker==self.squares[6]==self.squares[7]==self.squares[8]):
            return True
        else:
            return False
    
    def place_marker(self, player, position):
        position = int(position)
        self.squares[position] = player.marker
        
    def available_check(self, position):
        if(self.squares[position] == " "):
            return True
        else:
            return False
    
    def inboard_check(self, position):
        return position in [0,1,2,3,4,5,6,7,8]

    def boardfull_check(self):
        if(" " not in self.squares):
            print("Draw")
            return True    

class Player:
    def __init__(self,marker):
        self.marker = marker;
        
class Outputter:
    #from IPython.display import clear_output
    def display_board(self, board):
        for i in range(9):
            print(" %s "%(str(board.squares[i])),end="")
            if(i in [2,5,8]):
                print()
            else:
                print("|",end="")
    
    def print(self,s):
        print(s);
    
    def clear(self):
        pass
        #clear_output()

    def player_input(self, current_player):
        while(True):
            try:
                number = int(input(f"player {current_player} Enter your position:"))
            except ValueError:
                print("You must enter a number")
            else:
                return number
    
    def ask_playagain(self):
        while(True):
            in_playagain = input("Do u wanna play again?[Y/N]")
            if(in_playagain in ['Y','y','yes','YES','Yes']):
                return True
            elif(in_playagain in ['N','n','no','NO','No']):
                return False
            else:
                print('invalid input')    

game = Tictactoe()
game.playgame()