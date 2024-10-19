import argparse
import Iterator as I
import Annotation_create as a_c
import download_images as d_i












def arg_parser() -> argparse.Namespace:
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
    args = arg_parser()
    d_i.download_images(args.keyword,args.folder)
    a_c.create_annotation(args.folder, args.annotation)
    it: I.Iterator = I.Iterator(args.annotation)
    for val in it:
        print(val)


if __name__ == '__main__':
    main()
