# Converter for DOC, DOCX, XLS, XLSX, PPT,
# PPTX, EPS, TXT, RTF, HTML files to PDF

from abc import ABC, abstractmethod
# Typing
from io import BytesIO
from typing import BinaryIO

# Utils
import magic  # type: ignore
#  Conversion
from PIL import Image


class PdfConverter:
    __imgs_formats: tuple[str, ...]
    __file_converters: dict[str, "__AbstractConverter"]
    __converter: "__AbstractConverter"
    __save_path: str

    def __init__(self, save_path="./"):
        self.__save_path = self.__format_save_path(save_path)
        self.__imgs_formats = ("jpg", "jpeg", "png", "bmp")
        self.__file_converters = {
            "img": self.__ImageConverter(),
            # "other_file_type": self.OtherConverter, ...
        }

    @staticmethod
    def __format_save_path(save_path: str) -> str:
        if save_path[-1] != "/":
            return f"{save_path}/"
        return save_path

    def __choose_converter(self, source_data: BinaryIO) -> str:
        file_type: str = (
            (magic.from_buffer(source_data.read(), mime=True)).split("/")[-1]
        )
        if file_type in self.__file_converters:
            return file_type
        elif file_type in self.__imgs_formats:
            return "img"
        else:
            raise ValueError("Unsupported file format")

    def __create_file(self, file_name: str):
        file_path = f"{self.__save_path}{file_name}.pdf"
        with open(file_path, "a"):
            ...

    def __save_data(self, file_name: str, data: BytesIO):
        with open(f"{self.__save_path + file_name}.pdf", "wb") as file:
            file.write(data.getvalue())

    def convert(self, source_data: BinaryIO, result_name: str) -> BytesIO:
        converter_type: str = self.__choose_converter(source_data)
        self.__create_file(result_name)
        self.__converter = self.__file_converters[converter_type]
        result_data: BytesIO = self.__converter.convert(source_data)
        self.__save_data(file_name=result_name, data=result_data)
        return result_data

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
            with Image.open(source_data) as image:
                if image.mode == "RGBA":
                    image.convert("RGB")

                background = Image.new(
                    mode="RGB", size=self.__page_size_A4, color="white"
                )
                place: tuple[int, int] = (
                    int((background.size[0] - image.size[0]) / 2),
                    int((background.size[1] - image.size[1]) / 2),
                )
                background.paste(image, place)
                background.save(result_data, format="PDF")
            return result_data
