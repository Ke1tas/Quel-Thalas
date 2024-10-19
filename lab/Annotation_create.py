import csv
import os

def create_annotation(folder: str, annotation_path: str) -> None:
    """
    Создает файл аннотацию с абсолютными и относительными путями для элементов внутри данного пути.
    :param folder: Путь, по которому создается аннотация
    :param annotation_path: Путь к файлу аннотации
    :return:
    """
    if not os.path.exists(annotation_path):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_path}")
    if not os.path.exists(folder):
        raise FileNotFoundError(f"Файл аннотации не найден: {folder}")
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for filename in os.listdir(folder):
            writer.writerows([[os.path.abspath(os.path.join(folder, filename))],
                              [os.path.relpath(os.path.join(folder, filename), start=os.curdir)]])
