"""
this file will be responible for handling user input and displaying the current game state
"""


class GameState():
    def __init__(self):
        self.board = [
            #board is 8x8 2d list, each element of the list has 2 characters.
            #The first character represents the color of the piece, 'b' or 'w'.
            #The second character represents the type of the piece, 'K', 'Q', 'R', 'B', 'N', or 'p'.
            # "--" represents an empty space with no piece.
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whitemove = True
        self.moveLog = []