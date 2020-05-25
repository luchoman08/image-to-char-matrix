import unittest
from lib import validate_image, allowed_mime_types


class TestAllowedMimeTypes(unittest.TestCase):

    def test_validate_image(self):
        self.assertFalse(len(allowed_mime_types) is 0)
        self.assertTrue(validate_image(allowed_mime_types[0]))
        self.assertFalse(validate_image('text/html'))


if __name__ == '__main__':
    unittest.main()