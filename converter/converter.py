from typing import Callable, IO
import pathlib
import tempfile
import PyPDF2


# Converter for DOC, DOCX, XLS, XLSX, PPT, PPTX, PNG, JPG,
# JPEG, BMP, EPS, GIF, TXT, RTF, HTML files to PDF
class Converter:
    __pdf_reader: PyPDF2.PdfReader
    __pdf_writer: PyPDF2.PdfWriter = PyPDF2.PdfWriter()

    __conversion_methods: dict = {}

    def __init__(self):
        self.__conversion_methods = {
            "doc":  self.__doc_to_pdf,   "docx": self.__docx_to_pdf,
            "xls":  self.__xls_to_pdf,   "xlsx": self.__xlsx_to_pdf,
            "ppt":  self.__ppt_to_pdf,   "pptx": self.__pptx_to_pdf,
            "png":  self.__png_to_pdf,   "jpg":  self.__jpg_to_pdf,
            "jpeg": self.__jpeg_to_pdf,  "bmp":  self.__bmp_to_pdf,
            "eps":  self.__eps_to_pdf,   "gif":  self.__gif_to_pdf,
            "txt":  self.__txt_to_pdf,   "rtf":  self.__rtf_to_pdf,
            "html": self.__html_to_pdf,
        }

    # Methods for convert in_file to pdf
    @staticmethod
    def __doc_to_pdf(file):
        print("doc")

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
    def __png_to_pdf(file):
        print("png")

    @staticmethod
    def __jpg_to_pdf(file):
        print("jpg")

    @staticmethod
    def __jpeg_to_pdf(file):
        print("jpeg")

    @staticmethod
    def __bmp_to_pdf(file):
        print("bmp")

    @staticmethod
    def __eps_to_pdf(file):
        print("eps")

    @staticmethod
    def __gif_to_pdf(file):
        print("gif")

    @staticmethod
    def __txt_to_pdf(file):
        print("txt")

    @staticmethod
    def __rtf_to_pdf(file):
        print("rtf")

    @staticmethod
    def __html_to_pdf(file):
        print("html")

    @staticmethod
    def __extract_filetype(file_path: str) -> str:
        return pathlib.Path(file_path).suffix[1::]

    @staticmethod
    def __create_temporary_pdf() -> IO:
        return tempfile.TemporaryFile(mode="w", suffix="pdf")

    def __add_page(self, file) -> None:
        self.__pdf_reader = PyPDF2.PdfReader(file)
        page_count = len(self.__pdf_reader.pages)
        print(page_count)

    def convert(self, file_path: str, new_name: str = "result") -> object:
        file = self.__create_temporary_pdf()
        self.__conversion_methods[self.__extract_filetype(file_path)](file)


path = "/home/freiqq/Projects/Python/ToPdf/Klette_R._Computernoe_zrenie.Fragment.bmp"
converter = Converter()
# converter.convert(file_path=path)
converter.convert(file_path=path)
