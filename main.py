import pygame
from katarenga.constants import *
from katarenga.board import Board
from katarenga.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Katarenga")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:                  
                
                pos = pygame.mouse.get_pos()
                    
                row, col = get_row_col_from_mouse(pos)
                if game.turn == WHITE:
                    game.select(row, col)
                    
                # checking for scroll
                if event.button == 4:
                    attempt_advance = True
                    game.select(row, col, attempt_advance)  
                      
                game.select(row, col)

        
        game.update()
            
    pygame.quit()

main()

