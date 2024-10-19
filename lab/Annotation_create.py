import csv
import os

def create_annotation(folder: str, annotation_path: str) -> None:
    """
    Создает файл аннотацию с абсолютными и относительными путями для элементов внутри данного пути.
    :param folder: Путь, по которому создается аннотация
    :param annotation_path: Путь к файлу аннотации
    :return:
    """
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for filename in os.listdir(folder):
            writer.writerows([[os.path.abspath(folder) + '\\' + filename], [filename]])
