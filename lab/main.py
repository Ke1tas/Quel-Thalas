import argparse

import img as i
import img_combine as ic
import hist as h


def arg_parser() -> argparse.Namespace:
    """
    Получение аргументов из командной строки.
    :return: Возвращает полученные из командной строки аргументы.
    """
    parser = argparse.ArgumentParser(description='Скачивание изображений и создание аннотации.')
    parser.add_argument('--imgpath','-i', type=str, required=True, help='Путь к изображению.')
    parser.add_argument('--newimgpath','-ni', type=str, required=True,
                        help='Путь для сохранения нового изображения.')
    return parser.parse_args()


def main():
    try:
        args = arg_parser()
        img = i.img_load(args.imgpath)
        i.print_resolution(img)
        h.hist_show(img)
        combined_img = ic.combine_images(img,img)
        i.img_show(img)
        i.img_show(combined_img)
        i.img_save(combined_img,args.newimgpath)
    except Exception as exp:
        print(exp)


if __name__ == '__main__':
    main()
