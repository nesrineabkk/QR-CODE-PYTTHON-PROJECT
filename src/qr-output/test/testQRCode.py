import unittest
from qr_code import read_url, convert_url_into_qr_code

class TestQRCodeFunctions(unittest.TestCase):

    def test_read_url_correct(self , url):
       
        result = read_url(url)
        self.assertEqual(result, url)

    def test_read_url_incorrect(self , url):
        
        result = read_url(url)
        self.assertIsNone(result)

    def test_convert_url_into_qr_code(self , url):
    
        convert_url_into_qr_code(url)


