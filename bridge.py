# Пакетная обработка фотографий

import os
from PIL import Image

DIRECTORY = r"C:\Users\User\Desktop\Визуализация Эльдара Рязанова 4"
FROM_EXTENSION = ".jpg"
TO_EXTENSION = ".png"
MAX_SIZE = (700, 700)


def walk(find_directory):
    for root, dirs, files in os.walk(find_directory):  # рекурсивная функция
        for name in files:
            conversion(os.path.join(root, name))


def conversion(file):
    resize(file)
    name, extension = os.path.splitext(file)
    if extension == ".png" or extension == ".jpg":
        resize(file)
    if extension == FROM_EXTENSION:
        im = Image.open(file)
        im.save(name + TO_EXTENSION)
        os.remove(file)


def resize(file):
    try:
        im = Image.open(file)
        im.thumbnail(MAX_SIZE, Image.ANTIALIAS)  # сглаживание
        im.save(file)
    except:
        pass


if __name__ == "__main__":
    walk(DIRECTORY)