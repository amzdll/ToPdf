import os
from io import TextIOWrapper as File

import PyPDF2


# Converter for DOC, DOCX, XLS, XLSX, PPT, PPTX, PNG, JPG, JPEG, BMP, EPS, GIF, TXT, RTF, HTML files to PDF
class Converter:
    __pdf_reader: PyPDF2.PdfReader
    __pdf_writer: PyPDF2.PdfWriter = PyPDF2.PdfWriter()

    def __init__(self):
        ...

    @staticmethod
    def convert(self, file_path: str) -> object:
        ...

    def extract_filetype(self, file_path: str):
        ...

    def create_new_pdf(self) -> File:
        f = open('result.pdf', 'w')
        # self.add_page(f)
        print(type(f))
        return f;
        f.close()

    # todo: add types for parameters and result of methods
    def __add_page(self, file) -> None:
        self.__pdf_reader = PyPDF2.PdfReader(file)
        page_count = self.__pdf_reader.numPages
        print(page_count)


Converter.convert("file_path") -> bool


data -> result.pdf