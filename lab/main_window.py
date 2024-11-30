import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QMessageBox

import Iterator as It


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Monkey Viewer')
        self.setFixedSize(600, 400)

        self.layout = QVBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.layout.addWidget(self.image_label)

        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.clicked.connect(self.show_next_image)
        self.layout.addWidget(self.next_button)

        self.load_button = QPushButton("Загрузить файл аннотаций", self)
        self.load_button.clicked.connect(self.load_annotations)
        self.layout.addWidget(self.load_button)

        self.setLayout(self.layout)

        self.iterator = None

    def load_annotations(self)->None:
        """
        Загружает файл аннотации и передает его итератору.
        :return: None
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотаций", "",
                                                   "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            try:
                self.iterator = It.Iterator(file_name)
                self.show_next_image()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл аннотаций: {e}")

    def show_next_image(self) -> None:
        """
        Передает в image_label следующее изображение из файла аннотации
        :return: None
        """
        if self.iterator:
            try:
                image_path = next(self.iterator)
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    raise FileNotFoundError(f"Изображение по пути '{image_path}' не найдено.")
                self.image_label.setPixmap(pixmap)
            except StopIteration:
                self.image_label.setText("Изображения закончились")
            except FileNotFoundError as e:
                QMessageBox.critical(self, "Ошибка", str(e))
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при загрузке изображения: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())