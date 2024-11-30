import file_reader as f_r

class Iterator:
    # Класс итератор по абсолютным путям из файла аннотации

    def __init__(self, annotation_file: str) -> None:
        self.annotations = f_r.file_reader(annotation_file)
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