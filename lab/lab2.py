import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler


def mkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def download_images(keyword: str, folder: str)->None:
    mkdir(folder)
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder})
    google_crawler.crawl(keyword=keyword, max_num=50)


def create_annotation(folder: str,annotation_path: str)->None:
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for filename in os.listdir(folder):
            writer.writerows([[os.path.abspath(folder) + '\\' + filename],[filename]])


class Iterator:
    def __init__(self,annot_file: str):
        annotations = []
        with open(annot_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                annotations += row
    def __iter__ (self):
        for row in self.annotations:
            yield row['absolute_path'], row['relative_path']


def main():
    parser = argparse.ArgumentParser(description='Скачивание изображений и создание аннотации.')
    parser.add_argument('--keyword', type=str, required=True, help='Ключевое слово для поиска изображений.')
    parser.add_argument('--folder', type=str, required=True, help='Путь к папке для сохранения изображений.')
    parser.add_argument('--annotation', type=str, required=True, help='Путь к файлу аннотации (CSV).')

    args = parser.parse_args()

   # download_images(args.keyword,args.folder)
    create_annotation(args.folder,args.annotation)


if __name__ == '__main__':
    main()