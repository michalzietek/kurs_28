class BatchIterator:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            print("Nie mozesz juz iterowac")
        else:
            batch = self.data[self.index:self.index + self.batch_size]
            self.index += self.batch_size
            return batch


data = [item for item in range(100)]

batch_size = 10

batch_handler = BatchIterator(data=data, batch_size=batch_size)

print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
print(next(batch_handler))
