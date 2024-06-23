import unittest
from qr_code import read_url, convert_url_into_qr_code
#the test are Outside SRC  the dicrectory  

class TestQRCodeFunctions(unittest.TestCase):

    def test_read_url_correct(self):
        url = "https://google.com"
        result = read_url(url)
        self.assertEqual(result)

    def test_read_url_incorrect(self):
        url = "https://google.com"
        result = read_url(url)
        self.assertIsNone(result)

    def test_convert_url_into_qr_code(self):
        url = "https://google.com"
        convert_url_into_qr_code(url)


