import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler


def mkdir(folder: str) -> None:
    """
    Создает путь, если такового нет.
    :param folder: Данный путь.
    :return:
    """
    if not os.path.exists(folder):
        os.makedirs(folder)


def download_images(keyword: str, folder: str) -> None:
    """
    Загружает картинки по ключевому слову в заданную папку.
    :param keyword: Ключевое слово для поиска картинок.
    :param folder: Путь, куда сохраняются картинки.
    :return:
    """
    mkdir(folder)
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder})
    google_crawler.crawl(keyword=keyword, max_num=50)


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


class Iterator:
    # Класс итератор по абсолютным путям из файла аннотации

    def __init__(self, annotation_file: str) -> None:
        self.annotations = file_reader(annotation_file)
        self.counter = 0
        self.limit = len(self.annotations)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 2
            return self.annotations[self.counter - 2]
        else:
            raise StopIteration


def parse() -> argparse.Namespace:
    """
    Получение аргументов из командной строки.
    :return: Возвращает полученные из командной строки аргументы.
    """
    parser = argparse.ArgumentParser(description='Скачивание изображений и создание аннотации.')
    parser.add_argument('--keyword', type=str, required=True, help='Ключевое слово для поиска изображений.')
    parser.add_argument('--folder', type=str, required=True, help='Путь к папке для сохранения изображений.')
    parser.add_argument('--annotation', type=str, required=True, help='Путь к файлу аннотации (CSV).')
    return parser.parse_args()


def main():
    args = parse()
    create_annotation(args.folder, args.annotation)
    it: Iterator = Iterator(args.annotation)
    for val in it:
        print(val)


if __name__ == '__main__':
    main()
