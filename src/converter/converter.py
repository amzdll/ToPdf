# Converter for DOC, DOCX, XLS, XLSX, PPT,
# PPTX, EPS, GIF, TXT, RTF, HTML files to PDF

# Utils
import magic  # type: ignore

#  Conversion
from PIL import Image

# Typing
from io import BytesIO
from typing import BinaryIO

from abc import ABC, abstractmethod


class PdfConverter:
    __imgs_formats: tuple[str, ...]
    __file_converters: dict[str, '__AbstractConverter']
    __converter: '__AbstractConverter'

    def __init__(self):
        self.__imgs_formats = ("jpg", "jpeg", "png", "bmp")
        self.__file_converters = {
            "img": self.__ImageConverter(),
            # "other_file_type": self.OtherConverter, ...
        }

    def __choose_converter(self, source_data: BinaryIO) -> str:
        file_type: str = (
            (magic.from_buffer(source_data.read(), mime=True)).split("/")[-1]
        )
        if file_type in self.__file_converters:
            return file_type
        elif file_type in self.__imgs_formats:
            return "img"
        else:
            raise Exception("Unsupported file format")

    def convert(self, source_data: BinaryIO) -> BytesIO:
        converter_type: str = self.__choose_converter(source_data)
        self.__converter = self.__file_converters[converter_type]
        return self.__converter.convert(source_data)

    class __AbstractConverter(ABC):

        @abstractmethod
        def __init__(self):
            ...

        @abstractmethod
        def convert(self, source_data: BinaryIO) -> BytesIO:
            ...

    class __ImageConverter(__AbstractConverter):

        __page_size: tuple[int, int]

        def __init__(self):
            self.__page_size_A4 = (595, 842)

        def convert(self, source_data: BinaryIO) -> BytesIO:
            result_data: BytesIO = BytesIO()
            with (Image.open(source_data) as image):
                if image.mode == "RGBA":
                    image.convert("RGB")

                background = Image.new(
                    mode="RGB", size=self.__page_size_A4, color="white"
                )
                place: tuple[int, int] = (
                     int((background.size[0] - image.size[0]) / 2),
                     int((background.size[1] - image.size[1]) / 2)
                )
                background.paste(image, place)
                background.save(result_data, format="PDF")
            return result_data


# converter = PdfConverter()
# with (open("/test/data/images.png", "rb") as f,
#       open("result.pdf", "wb") as f2):
#     a = converter.convert(f)
#     f2.write(a.getvalue())