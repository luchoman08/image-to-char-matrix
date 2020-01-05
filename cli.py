import click
from lib import image_file_to_char_matrix, default_font, char_matrix_to_image


@click.group()
def cli():
    pass


@cli.command()
@click.option('--input-file')
@click.option('--output-file', default="output.jpg")
@click.option('--expected-width', default=None)
@click.option('--black-threshold', default=150)
@click.option('--char', default='X')
def generate(input_file, output_file, expected_width, black_threshold, char):
    """Takes an image input and write another image composed of black chars
    based in the black and white version of the input image
    """
    if expected_width is not None:
        expected_width = int(expected_width)

    matrix = image_file_to_char_matrix(input_file, expected_width, black_threshold, char)
    image = char_matrix_to_image(matrix, font=default_font)
    image.save(output_file)


if __name__ == "__main__":
    cli()
