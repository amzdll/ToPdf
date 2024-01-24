import unittest
import tempfile

from converter.converter import PdfConverter


class TestPdfConverter(unittest.TestCase):
    __converter: PdfConverter

    def setUp(self):
        self.__converter = PdfConverter()

    def test_incorrect_file_type(self) -> None:
        with (open("test/data/test.incorrect_format", "rb") as test_data,
              self.assertRaises(Exception)):
            self.__converter.convert(test_data)

    def test_image_conversion(self) -> None:
        result_file = tempfile.NamedTemporaryFile(suffix="pdf")
        expected_file = tempfile.NamedTemporaryFile(suffix="pdf")

        with (open("test/data/test.png", "rb") as test_data,
              open("test/data/result_png.pdf", "rb") as expected_data):
            result_file.write(self.__converter.convert(test_data).getvalue())
            expected_file.write(expected_data.read())

            self.assertEqual(result_file.read(), expected_file.read())


if __name__ == "__main__":
    unittest.main()
