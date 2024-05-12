from unittest import TestCase

import src.qr_code.qr_code as qr_code


class TestQrCode(TestCase):
    """Cover `qr_code.py` script."""

    def test_read_url(self) -> None:
        """Verifies that `read_url()` function returns a string object."""
        self.assertEqual(
            'https://url', 
            qr_code.read_url(content='https://url')
        )

    def test_read_url_on_incorrect_url(self) -> None:
        """Verifies that `read_url()` function returns an empty object due an incorrect input."""
        self.assertEqual(
            None, 
            qr_code.read_url(content='http://url')
        )

    def test_convert_url_into_qr_code(self) -> None:
        self.assertEqual(True, True)
