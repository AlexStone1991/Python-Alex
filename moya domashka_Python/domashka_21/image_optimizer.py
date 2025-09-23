import os
from PIL import Image
from tqdm import tqdm
import sys

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'JPG', 'JPEG'}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = 'WEBP'

def get_images_paths(source_path: str) -> list[str]:
    """
    Получает пути ко всем изображениям в директории.

    :param source_path: Путь к файлу или директории
    :return: Список путей к изображениям
    """
    image_paths = []

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Путь {source_path} не существует.")

    if os.path.isfile(source_path):
        if os.path.splitext(source_path)[1][1:] in ALLOWED_EXTENSIONS:
            image_paths.append(source_path)
    else:
        for root, _, files in os.walk(source_path):
            for file in files:
                if os.path.splitext(file)[1][1:] in ALLOWED_EXTENSIONS:
                    image_paths.append(os.path.join(root, file))

    return image_paths

def compress_image(image_path: str, output_format: str = DEFAULT_FORMAT, quality: int = DEFAULT_QUALITY) -> str:
    """
    Сжимает изображение в указанный формат и сохраняет его.

    :param image_path: Путь к исходному изображению
    :param output_format: Формат сжатия
    :param quality: Качество сжатия
    :return: Путь к сжатому файлу
    """
    if output_format not in {'WEBP'}:
        raise ValueError(f"Формат {output_format} не поддерживается.")

    image = Image.open(image_path)
    output_path = os.path.splitext(image_path)[0] + f".{output_format.lower()}"

    if output_format == 'WEBP':
        image.save(output_path, format='WEBP', quality=quality)

    return output_path

def main():
    """
    Управляет процессом обработки изображений и выводом прогресса.
    """
    if len(sys.argv) != 2:
        print("Использование: python image_optimizer.py <путь к директории или файлу>")
        return

    source_path = sys.argv[1]
    image_paths = get_images_paths(source_path)

    for image_path in tqdm(image_paths, desc="Обработка изображений"):
        try:
            compressed_path = compress_image(image_path)
            original_size = os.path.getsize(image_path)
            compressed_size = os.path.getsize(compressed_path)
            compression_ratio = (1 - compressed_size / original_size) * 100
            print(f"Изображение {image_path} сжато до {compressed_path} с коэффициентом сжатия {compression_ratio:.2f}%")
        except Exception as e:
            print(f"Ошибка при обработке изображения {image_path}: {e}")

if __name__ == "__main__":
    main()
