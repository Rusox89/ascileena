THRESHOLD = 128


def process_tuple(rgb):
    r, b, g = rgb
    return (r + b + g)/3


def process_square(square):
    val = sum(process_tuple(rgb) for row in square for rgb in row)
    num = sum(len(row) for row in square)

    return int(val / num)


def threshold(value):
    return '#' if value < THRESHOLD else ' '


def convert(square):
    return threshold(
        process_square(square)
    )


white_leena = [
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
]

black_leena = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
]


half_leena = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
]


assert process_square(half_leena) == 127
assert process_square(black_leena) == 0
assert process_square(white_leena) == 255
assert convert(half_leena) == '#'
assert convert(white_leena) == ' '
assert convert(black_leena) == '#'
