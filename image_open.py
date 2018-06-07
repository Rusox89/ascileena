from PIL import Image


def color_of_position(row_number, col_number, size_ascii_pixel, im):
    total_pixels = 0
    total_colors = (0, 0, 0)

    start_col_in_pixels = col_number*size_ascii_pixel
    start_row_in_pixels = row_number*size_ascii_pixel

    col_in_pixels = start_col_in_pixels
    row_in_pixels = start_row_in_pixels

    while col_in_pixels < (col_number+1)*size_ascii_pixel-1:
        print("col:",col_in_pixels,"row:", row_in_pixels)
        pixel = im.getpixel((col_in_pixels, row_in_pixels))

        total_colors = (total_colors[0] + pixel[0], total_colors[1] + pixel[1],
                total_colors[2]+pixel[2])

        col_in_pixels = col_in_pixels + 1
        total_pixels += 1

    print(total_colors)

    average = (total_colors[0]/total_pixels, total_colors[1]/total_pixels,
            total_colors[2]/total_pixels)
    return average

# file_name = '/Users/Russ/Downloads/20180103_194743.jpg'
file_name = 'Lenna_(test_image).png'
ascii_columns = 80

im = Image.open(file_name)
im_size = im.size
print(im.size)

image_data = (im.getdata())

width_of_a_pixel = int(im.size[0]/ascii_columns)
height_of_pixel = width_of_a_pixel

matrix = []

number_of_rows = int(im_size[1] / height_of_pixel)
for row_number in range(number_of_rows):
    row = []
    for col_number in range(ascii_columns):
        row.append(color_of_position(row_number, col_number, width_of_a_pixel,
            im))

    matrix.append(row)

print(matrix)
