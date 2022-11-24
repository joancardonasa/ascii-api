import numpy as np
from PIL import Image

import functools

import logging
logger = logging.getLogger(__name__)

DEFAULT_TARGET_WIDTH = 160

ASCII_BY_BRIGHTNESS = '`"i+tXZ*W$' #'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def process_image(image: Image, target_width: float = DEFAULT_TARGET_WIDTH) -> None:
    (raw_width, raw_height) = image.width, image.height

    if target_width < raw_width:
        target_height = int((raw_height / raw_width) * target_width)
        image = image.resize((target_width, target_height))

    pixel_matrix = np.asarray(image)
    brightness_matrix = np.mean(pixel_matrix, axis=2)
    norm_brightness_matrix = normalize_array_values_between_range(
        brightness_matrix, new_range=(0, len(ASCII_BY_BRIGHTNESS)-1))

    print(norm_brightness_matrix.shape)
    # (width, height) = (raw_im.width // 10, raw_im.height // 10)
    # im = raw_im.resize((width, height))
    # print("Successfully loaded image!")
    # print(f"Image size: {width}x{height}")

    # # Load an ndarray of (columns, rows, rgb[a])
    # # When a exists, what to do?
    # pixels = np.asarray(im)
    # print(pixels.shape)

    # # Average out each pixel by its rgb values. Should alpha be considered?
    # brightness_matrix = np.mean(pixels, axis=2)
    # normalized_brightness_matrix = normalize(brightness_matrix, new_range=(
    #     0, len(ASCII_BY_BRIGHTNESS)-1))

    # height, width = normalized_brightness_matrix.shape

    # img_string = ''
    # for i in range(height):
    #     for j in range(width):
    #         brightness_pixel_val = normalized_brightness_matrix[i, j]
    #         # We don't need to keep pixel brightness val
    #         #img_dict[(i, j)] = brightness_pixel_val
    #         img_string += ASCII_BY_BRIGHTNESS[int(brightness_pixel_val)] * 3
    # print(img_string)


def normalize_array_values_between_range(x, new_range=(0, 1)):
    if new_range == (0, 1): return(norm)

    xmin, xmax = np.min(x), np.max(x)
    norm = (x - xmin)/(xmax - xmin)

    return norm * (new_range[1] - new_range[0]) + new_range[0]


def map_to_ascii(pixel_value: float) -> str:
    pass
