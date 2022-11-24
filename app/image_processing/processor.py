import functools
import logging
import uuid

import numpy as np
from PIL import Image

logger = logging.getLogger(__name__)

PIXEL_TO_CHAR_SIZE_CORRECTION = 3
DEFAULT_TARGET_WIDTH = 80

ASCII_BY_BRIGHTNESS = "':i+tXZ*W$" #'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

RESULTDIR = 'tmp_result'


def process_image(image: Image, target_width: float = DEFAULT_TARGET_WIDTH) -> None:
    (raw_width, raw_height) = image.width, image.height

    if target_width < raw_width:
        target_height = int((raw_height / raw_width) * target_width)
        image = image.resize((target_width, target_height))

    pixel_matrix = np.asarray(image)
    brightness_matrix = np.mean(pixel_matrix, axis=2)
    norm_brightness_matrix = normalize_array_values_between_range(
        brightness_matrix, new_range=(0, len(ASCII_BY_BRIGHTNESS)-1))

    height, width = norm_brightness_matrix.shape

    output_file = f'../{RESULTDIR}/{uuid.uuid4()}'
    with open(output_file, 'w+') as text_file:
        for i in range(height):
            for j in range(width):
                brightness_pixel_val = norm_brightness_matrix[i, j]
                text_file.write(
                    ASCII_BY_BRIGHTNESS[int(brightness_pixel_val)] * PIXEL_TO_CHAR_SIZE_CORRECTION)
            text_file.write('\n')
    return output_file


def normalize_array_values_between_range(x, new_range=(0, 1)):
    if new_range == (0, 1): return(norm)

    xmin, xmax = np.min(x), np.max(x)
    norm = (x - xmin)/(xmax - xmin)

    return norm * (new_range[1] - new_range[0]) + new_range[0]
