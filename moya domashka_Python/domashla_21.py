from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
import pillow_avif
import os

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "dng"]

my_image = r"C:\Users\ALEXSTONE\Desktop\photo_2025-01-23_21-30-45.jpg"

# Регистрируем форматы
register_heif_opener()

source_path = r"C:\ALEXXX\Python Alex"

def compress_image(file_path: str, quality: int = 50, format: str = "avif") -> None:
    """
    Сжимает изображение в указанный формат с заданным качеством.

    :param file_path: Путь к исходному изображению.
    :param quality: Качество сжатия (по умолчанию 50).
    :param format: Формат сжатия (по умолчанию "avif").
    """
    # Поддерживаемые форматы
    supported_formats = ["webp", "heic", "avif"]

    # Проверка поддерживаемого формата
    if format not in supported_formats:
        raise ValueError(f"Формат {format} не поддерживается")
        
        # Открываем изображение
    image = Image.open(file_path)

    # Формируем новое имя файла
    new_file_path = os.path.splitext(file_path)[0] + f".{format}"

    if format in ["webp", "avif"]:
            image.save(new_file_path, format=format, quality=quality)
            return
    
    if format == "heic":
            heif_file = heif_from_pillow(image)
            heif_file.save(new_file_path, quality=quality)

def get_image_paths(source_path: str, allowed_extensions: list[str]) -> list[str]:
    """
    Возвращает список путей к изображениям с поддерживаемыми расширениями в указанной директории.

    :param source_path: Путь к директории или файлу.
    :param allowed_extensions: Список поддерживаемых расширений.
    :return: Список путей к изображениям.
    """
    if not os.path.exists(source_path):
        raise ValueError(f"Путь {source_path} не существует")

    if os.path.isfile(source_path):
        return [source_path]

    images = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                if file.split('.')[-1] in allowed_extensions:
                    images.append(full_path)

    return images