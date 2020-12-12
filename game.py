from main import computer_move,HumanPlayer,superComputer

class tictactoe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner=None

    def print_board(self):
        '''
        printing the board after move
        '''
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| "+" | ".join(row)+" |")
    @staticmethod
    def print_board_num():
        '''
        printing the number's onn the board to help user to choice
        '''
        board_num=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in board_num:
            print("| "+" | ".join(row)+" |")

    def available_moves(self):
        return [index for index,spot in enumerate(self.board) if spot==" "]
    
    def num_empty_square(self):
        return self.board.count(" ")

    def empty_square(self):
        return " " in self.board

    def make_move(self,square,letter):
        if self.board[square]==" ":
            self.board[square]=letter
            if self.game_winner(square,letter):
                self.current_winner=letter
            return True
        return False
    def game_winner(self,square,letter):
            #checking the row 
        row_ind=square//3
        row =self.board[row_ind*3:(row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True
            # checking the columns 
        col_ind=square%3
        col=self.board[col_ind*3:(col_ind+1)*3]
        if all([spot== letter for spot in col]):
            return True
            # chechking the diagonals
        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diagonal2]):
                return True
        return False
            
        


def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_board_num()
    letter="X"
    while game.empty_square():
        if letter=="O":
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter ,"moved to square", square)
                game.print_board()
            if game.current_winner:
                print(letter, "winner")
                return letter
        letter="X" if letter=="O" else "O"
    if print_game:
        print("it's a tie")

if __name__ == "__main__":
    pro=0
    noob=0
    tie=0
    for _ in range(5):
        t=tictactoe()
        x=HumanPlayer("X")
        o=computer_move("O")
        result=play(t,x,o,print_game=True)
        if result=="X":
            pro+=1
        elif result=="O":
            noob+=1
        else:
            tie+=1

    print(f"x is won round {pro} o won round {noob} rounds where {tie} tie")





























