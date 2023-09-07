import time
import pygame
import numpy as np

COLOR_DEAD = (10, 10, 10)
COLOR_BORN = (255, 255, 255)
COLOR_DIES = (170, 170, 170)
COLOR_GRID = (40, 40, 40)

def update(screen , cells, size, run = False):

    updatedCells = np.zeros((cells.shape[0], cells.shape[1]))

    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):

            aliveNeighbours = np.sum(cells[i-1:i+2, j-1:j+2]) - cells[i, j]
            color = COLOR_DEAD if cells[i, j] == 0 else COLOR_BORN

            if cells[i, j] == 1 and aliveNeighbours < 2:
                updatedCells[i, j] = 0
                if run:
                    color = COLOR_DIES

            elif cells[i, j] == 1 and aliveNeighbours > 3:
                updatedCells[i, j] = 0
                if run:
                    color = COLOR_DIES

            elif cells[i, j] == 0 and aliveNeighbours == 3:
                updatedCells[i, j] = 1
                if run:
                    color = COLOR_BORN

            else:
                updatedCells[i, j] = cells[i, j]

            pygame.draw.rect(screen, color, (i*size, j*size, size-1, size-1))

    return updatedCells      

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Game of Life")

    cells = np.zeros((100, 100))
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
                cells[x, y] = 1
                update(screen, cells, 10)
                pygame.display.update()
    
        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, 10, True)
            pygame.display.update()
        
        time.sleep(0.001)

if __name__ == "__main__":
    main()