from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
import numpy
from io import BytesIO

default_font = ImageFont.truetype("sans-serif.ttf", 20)


def char_matrix_to_image(char_matrix, font: FreeTypeFont):
    """Converts a  matrix of chars to image, the resultant image size
    depends on font size and char matrix length, for example, if char
    matrix has with equal to 15 and font size equal to 2, the resultant
    image width should be 20
    """
    font_size = font.size
    res = Image.new("RGB", tuple(i * font_size for i in (len(char_matrix[0]), len(char_matrix))), color=(255, 255, 255))
    draw = ImageDraw.Draw(res)

    col = 0
    r = 0

    for row in char_matrix:
        r = r + font_size
        for char in row:
            col = col + font_size
            draw.text((col, r), char, font=font, fill=(0, 0, 0))
        col = 0

    return res


def three_rule(a, b, c):
    return b*c/a


def scale(image_size, expected_width):
    """Returns the division between the image with over the expected width
    """
    return expected_width/image_size[0]


def image_to_char_matrix(image_bytes: BytesIO, expected_width=None, black_threshold=150, black_char="X", white_char="-"):
    """Function that converts an input image to a resultant image
    composed of chars based in the black and white version of the
    original image.

    If expected width in pixels is given, the resultant matrix
    width will be equal to the given value, and its height is
    obtained from a three rule over the width, expected width
    and the original height
    """
    im = Image.open(image_bytes)
    if expected_width is not None:
        image_size = im.size
        s = scale(image_size, expected_width)
        res_size = (int(image_size[0]*s), int(image_size[1]*s))
        im = im.resize(res_size)

    im = im.convert("L")
    im = im.point(lambda x: 0 if x < black_threshold else 255, '1')
    mat = numpy.array(im)
    res = []

    for row in mat:
        char_row = []
        for cell in row:
            if not cell:
                char_row.append(black_char)
            else:
                char_row.append(white_char)
        res.append(char_row)

    return res


def image_file_to_char_matrix(file_name: str, expected_width=None, black_threshold=150, black_char="X", white_char="-"):
    """Open image and return a char matrix based in the read files
    """
    image_bytes = open(file_name, 'rb')
    return image_to_char_matrix(image_bytes,
                                expected_width=expected_width,
                                black_threshold=black_threshold,
                                black_char=black_char,
                                white_char=white_char)


