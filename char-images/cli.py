import click
from lib import image_to_char_image


@click.group()
def cli():
    pass


@cli.command()
@click.option('--input-file', '-i', required=True)
@click.option('--output-file', '-o',  default="output.jpg")
@click.option('--expected-width', '-w', default=None)
@click.option('--show-preview', '-s', default=False)
@click.option('--black-threshold', '-t', default=150)
@click.option('--char', '-c', default='X')
def generate(input_file, output_file, expected_width, show_preview, black_threshold, char):
    """Takes an image input and write another image composed of black chars
    based in the black and white version of the input image
    """
    if expected_width is not None:
        expected_width = int(expected_width)

    image = image_to_char_image(input_file, expected_width, black_threshold, char)
    if show_preview:
        image.show()
    image.save(output_file)


if __name__ == "__main__":
    cli()
