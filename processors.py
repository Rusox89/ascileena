import logging


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



very_small_leena = [
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
    [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
]

assert process_square(very_small_leena) == 255
print(process_square(very_small_leena))
