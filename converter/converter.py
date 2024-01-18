from io import BytesIO
from typing import IO
import pathlib
import PyPDF2
from PIL import Image


# Converter for DOC, DOCX, XLS, XLSX, PPT, PPTX, PNG, JPG, JPEG, BMP, EPS, GIF, TXT, RTF, HTML files to PDF
class Converter:
    __pdf_reader: PyPDF2.PdfReader
    __pdf_merger: PyPDF2.PdfMerger = PyPDF2.PdfMerger()
    __pdf_writer: PyPDF2.PdfWriter = PyPDF2.PdfWriter()

    __conversion_methods: dict = {}
    __imgs_formats: tuple = ("jpg", "jpeg", "png", "bmp")

    def __init__(self):
        self.__conversion_methods = {
            "img": self.__img_to_pdf, "gif": self.__gif_to_pdf,
            "doc": self.__doc_to_pdf, "docx": self.__docx_to_pdf,
            "xls": self.__xls_to_pdf, "xlsx": self.__xlsx_to_pdf,
            "ppt": self.__ppt_to_pdf, "pptx": self.__pptx_to_pdf,
            "eps": self.__eps_to_pdf, "txt": self.__txt_to_pdf,
            "rtf": self.__rtf_to_pdf, "html": self.__html_to_pdf
        }

    # Methods for convert in_file to pdf
    @staticmethod
    def __img_to_pdf(source_data, result_data: BytesIO) -> None:
        print("hui")
        with Image.open(source_data) as image:
            if image.mode == "RGBA":
                image.convert("RGB")
            image.save(result_data, format="PDF")
        # path_to_save = "/Users/glenpoin/W/Projects/Python/ToPdf/converter/result.pdf"
        # with open(path_to_save, 'wb') as output_file:
        #     output_file.write(result_data.getvalue())

    #   fix
    @staticmethod
    def __gif_to_pdf(source_data, result_data: BytesIO) -> None:
        with Image.open(source_data) as gif:
            gif.save(result_data, save_all=True, append_images=gif.n_frames * [gif],
                     duration=gif.info['duration'], loop=0, format="PDF")
            gif.show()

    @staticmethod
    def __doc_to_pdf(source_file, result_file: IO) -> IO:
        print("doc")
        return result_file

    @staticmethod
    def __docx_to_pdf(file):
        print("docx")

    @staticmethod
    def __xls_to_pdf(file):
        print("xls")

    @staticmethod
    def __xlsx_to_pdf(file):
        print("xlsx")

    @staticmethod
    def __ppt_to_pdf(file):
        print("ppt")

    @staticmethod
    def __pptx_to_pdf(file):
        print("pptx")

    @staticmethod
    def __eps_to_pdf(file):
        print("eps")

    @staticmethod
    def __txt_to_pdf(file):
        print("txt")

    @staticmethod
    def __rtf_to_pdf(file):
        print("rtf")

    @staticmethod
    def __html_to_pdf(file):
        print("html")

    def __extract_filetype(self, file_path: str) -> str:
        file_type = pathlib.Path(file_path).suffix[1::]
        if file_type in self.__conversion_methods:
            return file_type
        elif file_type in self.__imgs_formats:
            return "img"

    def __add_page(self, file) -> None:
        self.__pdf_reader = PyPDF2.PdfReader(file)
        page_count = len(self.__pdf_reader.pages)
        print(page_count)

    def convert(self, file_name: str, source_data) -> BytesIO:
        result_data = BytesIO()
        self.__conversion_methods[self.__extract_filetype(file_name)](source_data, result_data)
        return result_data


# path = "/tests/test_img.png"
# converter = Converter()

# rd = converter.convert(source_file=path)

