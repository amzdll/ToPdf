import tempfile
from io import BytesIO
import pathlib
import PyPDF2
from PIL import Image
from typing import Callable, BinaryIO


# Converter for DOC, DOCX, XLS, XLSX, PPT, PPTX, EPS, GIF, TXT, RTF, HTML files to PDF
class Converter:
    __pdf_reader: PyPDF2.PdfReader
    __pdf_merger: PyPDF2.PdfMerger = PyPDF2.PdfMerger()
    __pdf_writer: PyPDF2.PdfWriter = PyPDF2.PdfWriter()

    __conversion_methods: dict[str, Callable]
    __imgs_formats: tuple = ("jpg", "jpeg", "png", "bmp")
    __docs_formats: tuple = ("doc", "docx")

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
    def __change_image_size(image_size: tuple) -> tuple[int, int]:
        return ((image_size[0] / 495) * image_size
                if image_size[0] >= image_size[1]
                else (image_size[0] / 742) * image_size)

    def __img_to_pdf(self, source_data, result_data: BytesIO) -> None:
        with Image.open(source_data) as image:
            if image.mode == "RGBA":
                image.convert("RGB")

            if image.size[0] > 495 or image.size[1] > 742:
                image.resize(self.__change_image_size(image.size))

            background = Image.new(mode="RGB", size=(595, 842), color="white")
            place: tuple[int, int] = (int((background.size[0] - image.size[0]) / 2),
                                      int((background.size[1] - image.size[1]) / 2))
            background.paste(image, place)
            background.save(result_data, format="PDF")

    @staticmethod
    def __gif_to_pdf(source_data, result_data: BytesIO) -> None:
        with Image.open(source_data) as gif:
            gif.save(result_data, save_all=True, append_images=gif.n_frames * [gif],
                     duration=gif.info['duration'], loop=0, format="PDF")
            gif.show()

    @staticmethod
    def __doc_to_pdf(source_file, result_file: BytesIO) -> None:
        print("doc")

    @staticmethod
    def __docx_to_pdf(source_data, result_data: BytesIO) -> None:
        print("docx")
        # result_data = docx2pdf.convert(source_data)

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

    #  fix: empty pdf, data is clear
    @staticmethod
    def __txt_to_pdf(source_data: BytesIO, result_data: BytesIO) -> BytesIO:
        return BytesIO()
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size=14)
        # pdf.write(5, source_data.read().decode("utf-8"))
        # pdf_output = pdf.output(dest='S').encode('utf-8')
        # result_data.seek(0)
        # result_data.write(pdf_output)
        # result_data.seek(0)
        # with open("result.pdf", "wb") as result_file:
        #     result_file.write(result_data.getvalue())
        #
        # return result_data

        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size=14)
        # pdf.write(5, source_data.read().decode("utf-8"))
        # # pdf.output("fdsa.pdf")
        # pdf_output = pdf.output(dest='S')
        # result_data = BytesIO(pdf_output.encode('utf-8'))
        # result_data.seek(0)
        # with open("result.pdf", "wb") as ffsda:
        #     ffsda.write(result_data.getvalue())

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
        else:
            return ""

    def __create_temporary_pdf(self):
        temporary_file = tempfile.NamedTemporaryFile(mode="wb", suffix="pdf")
        page = PyPDF2.PageObject.create_blank_page(width=595.276, height=841.891)
        self.__pdf_writer.add_page(page)
        with open(temporary_file.name, "wb") as f:
            self.__pdf_writer.write(f)
        return temporary_file

    def __add_page(self, file) -> None:
        self.__pdf_reader = PyPDF2.PdfReader(file)
        page_count = len(self.__pdf_reader.pages)
        print(page_count)

    def convert(self, file_name: str, source_data: BinaryIO) -> BytesIO:
        result_data = BytesIO()
        self.__conversion_methods[self.__extract_filetype(file_name)](source_data, result_data)
        return result_data


converter = Converter()
path = "/home/freiqq/Projects/Python/ToPdf/tests/resources/test.jpeg"
with open(path, "rb") as f:
    converter.convert("test.jpeg", f)

# if __name__ == "__main__":
#     converter = Converter()
#
#     path = "/Users/glenpoin/W/Projects/Python/ToPdf/tests/resources/test.txt"
#     f = open(path, "rb")
#     s_data = converter.convert(path, f)
