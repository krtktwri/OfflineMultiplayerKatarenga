import pygame
import numpy as np
from .constants import *
import random
from .piece import *

def board_setting():
    colors = np.zeros((8, 8), dtype=(float, 3))

    # Randomly assign values (0, 1, 2, 3) to specific squares within 2x2 blocks
    for i in range(0, 7, 2):
        for j in range(0, 7, 2):
            block = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
            np.random.shuffle(block)  # Shuffle the order of assignment
            colors[block[0]] = [RED, BLUE, GREEN, BROWN][0]
            colors[block[1]] = [RED, BLUE, GREEN, BROWN][1]
            colors[block[2]] = [RED, BLUE, GREEN, BROWN][2]
            colors[block[3]] = [RED, BLUE, GREEN, BROWN][3]

    return colors

class Board:
    def __init__(self):
        self.board = []
        self.grey_left = self.white_left = 8
        self.colors = board_setting()
        self.create_board()
        self.advanced_pieces = {GREY: 0, WHITE: 0}  # Track advanced pieces for each player
        

    def count_pieces(self, color):
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece.color == color:
                    count += 1
        return count
    
    def check_win_condition(self):
        grey_pieces_left = self.count_pieces(GREY)
        white_pieces_left = self.count_pieces(WHITE)

        if grey_pieces_left == 0:
            print("White wins!")
        elif white_pieces_left == 0:
            print("Grey wins!")
        elif self.advanced_pieces[GREY] == 2:
            print("Grey wins!")
        elif self.advanced_pieces[WHITE] == 2:
            print("White wins!")
    

    def display_message(self, win, message):
        text = self.font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text
        win.blit(text, text_rect)
                
    def draw_squares(self, win):
        win.fill(GREY)
        for row in range(ROWS):
            for col in range(COLS):
                # choosing a random color for the rectangle
                pygame.draw.rect(win, self.colors[col, row], (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
    def get_piece(self, row, col):
        return self.board[row][col]
                
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(Piece(row, col, GREY))
                elif row == 7:
                    self.board[row].append(Piece(row, col, WHITE))
                else:
                    self.board[row].append(0)
                    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
        
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
    
    def get_valid_moves(self, piece):
        
        # Clear the previous valid moves
        self.clear_previous_valid_moves()
        
        # Checking the color of the square
        square_color = self.colors[piece.row, piece.col]
        moves = {}
        row = piece.row
        col = piece.col
        
        # getting valid moves for the piece which moves like a king  
        if np.array_equal(square_color, RED):           
            # populating moves with possible king_moves
            moves.update(self.king_moves(row, col))
    
        if np.array_equal(square_color, BLUE):
            # populating moves with possible rook_moves
            moves.update(self.rook_moves(row, col))
        
        if np.array_equal(square_color, GREEN):
            # populating moves with possible bishop_moves
            moves.update(self.bishop_moves(row, col))
        
        if np.array_equal(square_color, BROWN):
            # populating moves with possible knight_moves
            moves.update(self.knight_moves(row, col))
                    
        return moves
    
    def king_moves(self, row, col):
        moves = {}

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if self.board[r][c] == 0:
                        moves[(r, c)] = []
                    elif self.board[r][c].color != self.board[row][col].color:
                        moves[(r, c)] = []
                        capture = True
        return moves
    
    def rook_moves(self, row, col):
        moves = {}

        square_color = self.colors[row, col]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left        

        for dx, dy in directions:
            r, c = row + dx, col + dy
            
            
            while 0 <= r < ROWS  and 0 <= c < COLS:
                
                if self.board[r][c] == 0:
                    moves[(r, c)] = []
                
                elif (self.board[r][c].color != self.board[row][col].color):
                    moves[(r, c)] = []
                    break
                elif (self.color[r, c] == BLUE
                    moves[(r, c)] = []
                    break
                
                
                else:
                    break
                r += dx
                c += dy


        return moves

                      
    
    def bishop_moves(self, row, col):
        moves = {}
        

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions

        for dx, dy in directions:
            r, c = row + dx, col + dy
            while 0 <= r < ROWS and 0 <= c < COLS:
                if self.board[r][c] == 0:
                    moves[(r, c)] = []
                elif self.board[r][c].color != self.board[row][col].color:
                    moves[(r, c)] = []
                    capture = True
                    break
                elif self.color[r][c] == GREEN
                    moves[(r, c)] = []
                    break
                else:
                    break
                r += dx
                c += dy

        return moves
    
    def knight_moves(self, row, col):
        moves = {}

        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]  # Possible knight moves

        for dx, dy in knight_moves:
            r, c = row + dx, col + dy
            if 0 <= r < ROWS and 0 <= c < COLS:
                if self.board[r][c] == 0 or self.board[r][c].color != self.board[row][col].color:
                    moves[(r, c)] = []

        return moves
                
    def clear_previous_valid_moves(self):
        capture = False
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.valid_moves = {}  # Assuming valid_moves is a dictionary attribute in the Piece class
                
