# import math
import random
class player:
    def __init__(self,letter):
        self.letter=letter

class  computer_move(player):
    """
    computer choices randomly
    """
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square


class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+"Move Enter in betweeen 0,8:")
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("Invalid square, Try again!")

        return val


























# import random


# class player:
#     def __init__(self,letter):
#         self.letter=letter
        
# class computerMove(player):
#     def __init__(self,letter):
#         super().__init__(letter)
#     def get_move(self,game):
#         num=random.choice(game.available_moves())
#         return num

# class HumanMove(player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self,game):
#         valid_move=False
#         val=None
#         while not valid_move:
#             user_num=input(self.letter, "Enter number bw 0 to 8:")
#             try:
#                 val=int(user_num)
#                 if user_num not in game.available_moves():
#                     raise ValueError
#                 valid_move=False
#             except ValueError:
#                 print("try again")

#         return val

                    





        
        















































