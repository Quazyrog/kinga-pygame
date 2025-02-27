class Level:
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self._tiles = tiles

    def __getitem__(self, coord):
        x, y = coord
        return self._tiles[x][y]

    def __setitem__(self, coord, value):
        x, y = coord
        self._tiles[x][y] = value


def get_empty_level(width, height, fill):
    tiles = []
    for x in range(width):
        new_column = []
        for y in range(height):
            new_column.append(fill)
        tiles.append(new_column)
    return Level(width, height, tiles)


def get_arena_level(width, height):
    level = get_empty_level(width, height, "water")

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            level[x, y] = "grass"  # to samo, co: level.__setitem__((x, y), "brick")

    for x in range(2, width - 2):
        for y in range(2, height - 2):
            level[x, y] = "brick"

    for x in range(3, width - 3):
        for y in range(3, height - 3):
            level[x, y] = "grass"

    return level


def load_level(filename):
    input_file = open(filename)
    # TODO read width and height
    width = 7
    height = 6
    lvl = get_empty_level(width, height, "water")

    y = 0
    for line in input_file:
        line = line.strip()
        line = line.split(",")

        x = 0
        for e in line:
            if e == "g":
                lvl[x, y] = "grass"
            elif e == "b":
                lvl[x, y] = "brick"
            elif e == "w":
                lvl[x, y] = "water"
            x += 1

        y += 1

    input_file.close()
    return lvl
