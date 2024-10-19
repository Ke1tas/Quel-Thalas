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
