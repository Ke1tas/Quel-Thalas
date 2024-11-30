import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
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

    def load_annotations(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотаций", "",
                                                   "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            self.iterator = It.Iterator(file_name)
            self.show_next_image()  # Показываем первое изображение

    def show_next_image(self):
        if self.iterator:
            try:
                image_path = next(self.iterator)
                pixmap = QPixmap(image_path)
                self.image_label.setPixmap(pixmap)
            except StopIteration:
                self.image_label.setText("Изображения закончились")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())