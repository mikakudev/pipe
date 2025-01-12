import pygame

CELL_SIZE = 100

pipe_images = {
    "straight": pygame.image.load("assets/images/straight.png"),
    "corner": pygame.image.load("assets/images/corner.png"),
    "t_shaped": pygame.image.load("assets/images/t_shaped.png"),
    "end": pygame.image.load("assets/images/end.png"),
}

for key in pipe_images:
    pipe_images[key] = pygame.transform.scale(pipe_images[key], (CELL_SIZE, CELL_SIZE))


class Pipe:
    def __init__(self, x, y, pipe_type, rotation=0):
        self.x = x
        self.y = y
        self.type = pipe_type
        self.rotation = rotation
        self.base_image = pipe_images[self.type]

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.base_image, -self.rotation)
        rect = rotated_image.get_rect(center=(self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2))
        screen.blit(rotated_image, rect.topleft)

    def rotate(self):
        self.rotation = (self.rotation + 90) % 360
