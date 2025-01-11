import pygame
from pipes import Pipe
from pipes import pipe_images

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
CELL_SIZE = 80
GRID_ROWS = 6   # Количество строк
GRID_COLS = 6   # Количество столбцов

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Водопровводныые трубы")
clock = pygame.time.Clock()

grid = [[None for _ in range(6)] for _ in range(6)]
grid[2][2] = Pipe(2 * CELL_SIZE, 2 * CELL_SIZE, "straight")

def draw_grid():
    for row in range(6):
        for col in range(6):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (200,200,200), rect, 1)

def draw_pipes():
    for row in grid:
        for pipe in row:
            if pipe:
                pipe.draw(screen)

def handle_click(pos):
    col = pos[0] // CELL_SIZE
    row = pos[1] // CELL_SIZE
    if 0 <= row < 6 and 0 <= col < 6 and grid[row][col]:
        grid[row][col].rotate()

# ОСновной игроговой цикл

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = mouse_x // CELL_SIZE
            row = mouse_x // CELL_SIZE

            if 0 <= GRID_ROWS and 0 <= col < GRID_COLS:
                pipe = grid[row][col]
                if pipe:
                    pipe.rotate()

    screen.fill((0,0,0))
    draw_grid()
    draw_pipes()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
