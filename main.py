import pygame
from pipes import Pipe
from levels import levels

"""Параметры экрана"""
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 900
FPS = 60
CELL_SIZE = 100
GRID_ROWS,GRID_COLS = 8, 8    # Количество строк

"""Инициализация Pygame"""
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Водопровводныые трубы")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 36)

"""Глобальные переменные"""
current_level = 0
grid = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

time_remaining = 60



"""Функиции"""
"""Рисует сетку на экране"""
def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * CELL_SIZE, (row + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (200,200,200), rect, 1)

"""Отрисовка труб"""
def draw_pipes():
    for row in grid:
        for pipe in row:
            if pipe:
                pipe.draw(screen)

"""обработки нажатий пользователя"""
def handle_click(pos):
    col = pos[0] // CELL_SIZE
    row = (pos[1] - 100) // CELL_SIZE
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS and grid[row][col]:
        grid[row][col].rotate()

"""Загрузка уровня по индексу и заполнение сетки трубами"""
def load_level(level_index):
    global grid
    level = levels[level_index]
    for row in range(len(level)):
        for col in range(len(level[row])):
            pipe_type = level[row][col]
            if pipe_type:
                grid[row][col] = Pipe(col * CELL_SIZE, (row + 1) * CELL_SIZE, pipe_type)

def check_level_complete():
    return False

def next_level():
    global current_level, grid
    current_level += 1
    if current_level < len(leveld):
        grid = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        load_level(current_level)
    else:
        print("Вы прошли все уровние игра окончена")
        pygame.quit()
        exit()

# загружаем первый уровень
load_level(current_level)


# ОСновной игроговой цикл
running = True
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)

        if event.type == timer_event:
            time_remaining -= 1
            if time_remaining <= 0:
                print("Время истекло")
                running = False

        timer_text = font.render(f"Время : {time_remaining}",True, (255,0,0))



    if check_level_complete():
        next_level()

    screen.fill((0,0,0))
    screen.blit(timer_text, (10, 10))
    draw_grid()
    draw_pipes()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
