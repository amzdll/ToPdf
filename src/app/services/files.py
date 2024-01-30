from typing import BinaryIO

from src.app.core.config import get_app_settings
from src.utils import converter
from src.utils.converter import PdfConverter

settings = get_app_settings()
imgs_storage_path: str = settings.imgs_storage_path


class FilesService:
    __converter: PdfConverter = PdfConverter(imgs_storage_path)

    @staticmethod
    async def extract_filename(file: str) -> str:
        return file.split(".")[0]

    async def convert_file(
            self,
            user_id: str,
            filename: str,
            source_data: BinaryIO
    ):
        self.__converter.convert(
            source_data=source_data,
            result_name=f"{"user_id_" + user_id + "_" + str(filename)}")


files_service = FilesService()
