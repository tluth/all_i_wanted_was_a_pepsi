"""
basic.py
Basic image processing functions for the image_processing library.
"""

import random
from typing import Tuple

from PIL import Image


def calculate_luminance(r: int, g: int, b: int) -> float:
    """Calculate the luminance (perceived brightness) of an RGB pixel.

    Args:
        r (int): Red channel value (0-255).
        g (int): Green channel value (0-255).
        b (int): Blue channel value (0-255).

    Returns:
        float: Luminance value (0-255).
    """
    return 0.299 * r + 0.587 * g + 0.114 * b


def add_noise_to_extremes(
    image: Image.Image,
    noise_limit: int = 10,
    white_threshold: int = 240,
    black_threshold: int = 10,
) -> Image.Image:
    """Add random noise to pixels close to white or black.

    For each pixel, if all RGB values are >= white_threshold (close to white) or <= black_threshold (close to black),
    add random noise within [-noise_limit, noise_limit] to each channel.

    Args:
        image (PIL.Image.Image): The input image (mode 'RGB').
        noise_limit (int): Maximum absolute value of noise to add to each channel (default 10).
        white_threshold (int): Lower bound for white pixel detection (default 245).
        black_threshold (int): Upper bound for black pixel detection (default 10).

    Returns:
        PIL.Image.Image: The image with noise added to extreme pixels.
    """
    if image.mode != "RGB":
        image = image.convert("RGB")
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            luminance = calculate_luminance(r, g, b)
            if luminance >= white_threshold or luminance <= black_threshold:
                r_new = min(255, max(0, r + random.randint(-noise_limit, noise_limit)))
                g_new = min(255, max(0, g + random.randint(-noise_limit, noise_limit)))
                b_new = min(255, max(0, b + random.randint(-noise_limit, noise_limit)))
                pixels[x, y] = (r_new, g_new, b_new)
    return image
