THRESHOLDS = {
    36: ' ',
    72: '.',
    108: 'o',
    144: 'O',
    180: '0',
    216: 'X',
    255: '#',
}

CONVERSION_ARRAY = THRESHOLDS.keys()


def float_to_character(f):
    lower_t = 0
    for higher_t in CONVERSION_ARRAY:
        if higher_t > f >= lower_t:
            return THRESHOLDS[higher_t]
        lower_t = higher_t
    return THRESHOLDS[higher_t]


def process_tuple(rgb):
    r, b, g = rgb
    return (r + b + g)/3


def process_square(square):
    val = sum(process_tuple(rgb) for row in square for rgb in row)
    num = sum(len(row) for row in square)

    return int(val / num)


def threshold(value):
    return '#' if value < THRESHOLDS else ' '


def convert(square):
    return [
        [
            float_to_character(process_tuple(pixel))
            for pixel in row
        ]
        for row in square
    ]


#  white_leena = [
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#  ]

#  black_leena = [
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#  ]


#  half_leena = [
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#      [(0, 0, 0), (0, 0, 0), (0, 0, 0)],
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#      [(255, 255, 255), (255, 255, 255), (255, 255, 255)],
#  ]


#  assert process_square(half_leena) == 127
#  assert process_square(black_leena) == 0
#  assert process_square(white_leena) == 255
#  assert convert(half_leena) == '#'
#  assert convert(white_leena) == ' '
#  assert convert(black_leena) == '#'

#  assert float_to_character
