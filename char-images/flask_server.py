from flask import Flask, request, jsonify, send_file
from lib import image_to_char_image
from io import BytesIO
app = Flask(__name__)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


class Error:
    def __init__(self, message: str, short_name: str,  error_code: int):
        self.message = message
        self.short_name = short_name
        self.error_code = error_code

    def to_json(self):
        return {'message': self.message, 'short_name': self.short_name, 'error_code': self.error_code}


expected_width_non_numeric = Error("expected width should be a number", "invalid_input", 1)
black_threshold_non_numeric = Error("expected black threshold should be a number", "invalid_input", 2)


@app.route('/char-image', methods=['POST'])
def char_image():
    """Char image allow to upload a file with some config
    params and return as response a image composed of chars
    based on the black and white version of the original
    uploaded image.
    """
    image = request.files['image']

    expected_width = request.form.get('expected_width')
    if not expected_width.isdigit():
        return jsonify(expected_width_non_numeric.to_json())

    black_threshold = request.form.get('black_threshold')
    if black_threshold is not None and not black_threshold.isdigit():
        return jsonify(black_threshold_non_numeric.to_json())

    if black_threshold is not None:
        black_threshold = int(black_threshold)
        response = image_to_char_image(image.stream, int(expected_width), black_threshold)
        return serve_pil_image(response)

    response = image_to_char_image(image.stream, int(expected_width))
    return serve_pil_image(response)
