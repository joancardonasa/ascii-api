import numpy as np
from PIL import Image

import functools

def check_image_size(filename: str) -> None:
    im = Image.open(filename)
    print("Successfully loaded image!")
    print(f"Image size: {im.size[0]}x{im.size[1]}")

    # Load an ndarray of (columns, rows, rgb[a])
    # When a exists, what to do?
    pixels = np.asarray(im)
    print(pixels.shape)

    # Average out each pixel by its rgb values. Should alpha be considered?
    pixel_matrix = np.mean(pixels, axis=2)
    print(pixel_matrix.shape)
