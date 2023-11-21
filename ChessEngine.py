""" Reponsible to store all the 
information about the current state of a Chess game"""

""" Also Determining the valid moves of the current state. Keeping a move log"""

class gameState():
    def __init__(self):
        # board is 8x8 2D List, b is Black, w is for White, Big letters are for chess names
         self.board = [
             ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
             ["bp", "bp", "bp", "bp", "bp", "bp", "bp","bp"],
             ["--","--","--","--","--","--","--","--"],
             ["--","--","--","--","--","--","--","--"],
             ["--","--","--","--","--","--","--","--"],
             ["--","--","--","--","--","--","--","--"],
             ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
             ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
              
             ]
         
         self.whiteToMove = True
         self.moveLog = []
        
        


