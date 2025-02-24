import pygame


class Globals:
    running = True
    width = 1280
    height = 720
    scale_value = 3
    tile_base_size = 32
    grass_texture = None


class Level:
    def __init__(self):
        self.width = 3
        self.height = 2
        self._tiles = [["grass", "brick"], ["water", "grass"], ["water", "grass"]]

    def __getitem__(self, coord):
        x, y = coord
        return self._tiles[x][y]


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.running = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((Globals.width, Globals.height))

    Globals.grass_texture = pygame.image.load('assets/grass.png')
    Globals.grass_texture = pygame.transform.scale_by(Globals.grass_texture, Globals.scale_value)
    Globals.water_texture = pygame.image.load('assets/water.png')
    Globals.water_texture = pygame.transform.scale_by(Globals.water_texture, Globals.scale_value)
    Globals.brick_texture = pygame.image.load('assets/brick.png')
    Globals.brick_texture = pygame.transform.scale_by(Globals.brick_texture, Globals.scale_value)

    l = Level()
    while Globals.running:
        handle_events()
        screen .fill("black")
        for level_y in range(l.height):
            for level_x in range(l.width):
                tile_x = level_x * Globals.tile_base_size * Globals.scale_value
                tile_y = level_y * Globals.tile_base_size * Globals.scale_value
                texture = None
                if l[level_x, level_y] == "grass":
                    texture = Globals.grass_texture
                if l[level_x, level_y] == "water":
                    texture = Globals.water_texture
                if l[level_x, level_y] == "brick":
                    texture = Globals.brick_texture
                screen.blit(texture, (tile_x, tile_y))
        pygame.display.flip()

    pygame.quit()


main()
