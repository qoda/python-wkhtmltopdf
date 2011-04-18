import os
import unittest

from main import WKhtmlToPdf

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.wkhtmltopdf = WKhtmlToPdf(url="http://www.example.com", output_file="/tmp/example.pdf")
    
    def test_wkhtmltopdf(self):
        print self.wkhtmltopdf._create_option_list()
    
    def tearDown(self):
        try:
            os.remove('/tmp/example.pdf')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()