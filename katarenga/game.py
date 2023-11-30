import pygame
from katarenga.constants import *
from katarenga.board import Board
import numpy as np

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def _init():
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        
    def advance_piece(self, piece):
        if np.array_equal(piece.color, WHITE) and piece.row == 0:
            self.board.advanced_pieces[WHITE] += 1
            self.board.remove([piece])
            self.change_turn()            
            self.board.check_win_condition()

        elif np.array_equal(piece.color, GREY) and piece.row == 7:
            self.board.advanced_pieces[GREY] += 1
            self.board.remove([piece])
            self.change_turn()
            self.board.check_win_condition()
        else:
            pass
        
    def reset(self):
        self._init()
        pass
        
    def select(self, row, col, attempt_advance=False):

        if self.selected:
            result = self._move(row, col)

            if not result:
                self.selected = None
                self.select(row, col)
            
            if attempt_advance:
                print("attempting to advance piece")
                self.advance_piece(self.selected)
                self.selected = None

        piece = self.board.get_piece(row, col)

                            
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
    
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
            self.board.check_win_condition()
        # If capture == True, then the removing opposite color piece from the board
        elif self.selected and piece != 0 and (row, col) in self.valid_moves:
            self.board.remove([piece])
            self.board.move(self.selected, row, col)
            self.change_turn()
            self.board.check_win_condition()

        else:
            return False

        return True
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, P2, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves ={}
        if self.turn == GREY:
            self.turn = WHITE
        else:
            self.turn = GREY
        
 