import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    supported_formats = ('.jpg', '.jpeg', '.png')

    def __init__(self, quality: int):
        """
        Конструктор класса для инициализации качества сжатия.

        Args:
            quality (int): Качество сжатия изображения.
        """
        self.__quality = quality

    @property
    def quality(self) -> int:
        """
        Геттер для получения значения качества сжатия.

        Returns:
            int: Качество сжатия.
        """
        return self.__quality

    @quality.setter
    def quality(self, quality: int) -> None:
        """
        Сеттер для установки значения качества сжатия.

        Args:
            quality (int): Новое значение качества сжатия.
        """
        self.__quality = quality

