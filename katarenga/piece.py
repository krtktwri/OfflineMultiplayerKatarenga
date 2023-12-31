from .constants import RED, WHITE, GREY, SQUARE_SIZE, BLACK
import pygame

class Piece:
    
    PADDING = 25
    OUTLINE = 4
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        
        if self.color == WHITE:
            self.direction = -1
        else:
            self.direction = 1
            
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) 
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)