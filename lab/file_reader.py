import csv
import os

def file_reader(annotation_file: str) -> list:
    """
    Считывает строки из файла и записывает их в массив
    :param annotation_file: путь к файлу
    :return: массив строк из файла
    """
    if not os.path.exists(annotation_file):
        raise FileNotFoundError(f"Файл аннотации не найден: {annotation_file}")
    annotations = []
    with open(annotation_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            annotations += row
    return annotations


