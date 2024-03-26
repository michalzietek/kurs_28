class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

data = [1, 2, 3, 4, 5]

my_iterable = MyIterable(data)
for item in my_iterable:
    print(item)

for item in my_iterable:
    print(item)

# def fast_generator(data):
#     for item in data:
#         yield item
#
# generator = fast_generator(data)
# for item in range(100):
#     next(generator)

