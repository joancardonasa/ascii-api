import numpy as np
from PIL import Image

import functools

ASCII_BY_BRIGHTNESS = '`"i+tXZ*W$' #'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

def normalize(x, new_range=(0, 1)): #x is an array. Default range is between zero and one
    xmin, xmax = np.min(x), np.max(x) #get max and min from input array
    norm = (x - xmin)/(xmax - xmin) # scale between zero and one

    if new_range == (0, 1):
        return(norm) # wanted range is the same as norm
    elif new_range != (0, 1):
        return norm * (new_range[1] - new_range[0]) + new_range[0]


def map_to_ascii(brightness: float) -> str:
    pass


def check_image_size(filename: str) -> None:
    raw_im = Image.open(filename)
    (width, height) = (raw_im.width // 4, raw_im.height // 4)
    im = raw_im.resize((width, height))
    print("Successfully loaded image!")
    print(f"Image size: {width}x{height}")

    # Load an ndarray of (columns, rows, rgb[a])
    # When a exists, what to do?
    pixels = np.asarray(im)
    print(pixels.shape)

    # Average out each pixel by its rgb values. Should alpha be considered?
    brightness_matrix = np.mean(pixels, axis=2)
    normalized_brightness_matrix = normalize(brightness_matrix, new_range=(
        0, len(ASCII_BY_BRIGHTNESS)-1))

    height, width = normalized_brightness_matrix.shape

    img_string = ''
    for i in range(height):
        for j in range(width):
            brightness_pixel_val = normalized_brightness_matrix[i, j]
            # We don't need to keep pixel brightness val
            #img_dict[(i, j)] = brightness_pixel_val
            img_string += ASCII_BY_BRIGHTNESS[int(brightness_pixel_val)]
    print(img_string)
