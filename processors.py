import logging


THRESHOLD = 128

def process_tuple(rgb):
    r, b, g = rgb
    return (r + b + g)/3

def process_square(square):
    width = len(square)
    try:
        height = len(square[0])
    except IndexError as e:
        logging.error("Square received " + str(square))
        raise
    
    val = sum(process_tuple(rgb) for row in square for rgb in row)
    num = sum(len(row) for row in square)

    return int(val / num)


def threshold(value):
    return '#' if value < THRESHOLD else ' '


def convert(square):
    return threshold(
        process_square(square)
    )

very_small_leena = [
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
]

white_leena = [
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
    [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
]




assert process_square(white_leena) == 0
assert process_square(very_small_leena) == 255
assert convert(very_small_leena) == '#'
assert convert(white_leena) == ' '
