import pytest
import tempfile
from src.utils.converter import PdfConverter


@pytest.fixture
def pdf_converter():
    return PdfConverter()


def test_incorrect_file_type(pdf_converter):
    with open("test/data/test.incorrect_format", "rb") as test_data:
        with pytest.raises(Exception):
            pdf_converter.convert(test_data)


def test_image_conversion(pdf_converter):
    result_file = tempfile.NamedTemporaryFile(suffix="pdf")
    expected_file = tempfile.NamedTemporaryFile(suffix="pdf")

    with open("test/data/test.png", "rb") as test_data, open(
        "test/data/result_png.pdf", "rb"
    ) as expected_data:
        result_file.write(pdf_converter.convert(test_data).getvalue())
        expected_file.write(expected_data.read())

        assert result_file.read() == expected_file.read()
