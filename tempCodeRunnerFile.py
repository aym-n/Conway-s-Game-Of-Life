import time
import pygame
import numpy as np

COLOR_ALIVE = (255, 255, 255)
COLOR_DEAD = (10, 100, 10)
COLOR_BORN = (0, 255, 0)
COLOR_DIES = (255, 0, 0)
COLOR_GRID = (128, 128, 128)

def update(screen , cells, size, run = False):

    updatedCells = np.zeros((cells.shape[0], cells.shape[1]))

    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):

            aliveNeighbours = np.sum(cells[i-1:i+2, j-1:j+2]) - cells[i, j]
            color = COLOR_DEAD if cells[i, j] == 0 else COLOR_BORN
                
            if cells[i, j] == 1:
                if aliveNeighbours < 2 or aliveNeighbours > 3:
                    if run:
                        color = COLOR_DIES
                elif aliveNeighbours >= 2 and aliveNeighbours <= 3:
                    updatedCells[i, j] = 1
                    if run:
                        color = COLOR_ALIVE
            else:
                if aliveNeighbours == 3:
                    updatedCells[i, j] = 1
                    if run:
                        color = COLOR_BORN

            pygame.draw.rect(screen, color, (i*size, j*size, size-1, size-1))

    return updatedCells      

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game of Life")

    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = x // 10
                y = y // 10
                cells[x, y] = 145
                update(screen, cells, 10)
                pygame.display.update()
    
        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10, True)
            pygame.display.update()
        
        time.sleep(0.001)

if __name__ == "__main__":
    main()