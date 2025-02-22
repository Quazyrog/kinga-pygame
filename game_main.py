import pygame

class Globals:
    running = True
    width = 1280
    height = 720
    grass_texture = None


class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.running = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((Globals.width, Globals.height))

    Globals.grass_texture = pygame.image.load('assets/grass.png')

    while Globals.running:
        handle_events()
        screen .fill("black")
        x = 0
        y = 0
        while y < Globals.height:
            while x < Globals.width:
                screen.blit(Globals.grass_texture, (x, y))
                x += 32
            x = 0
            y += 32
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
