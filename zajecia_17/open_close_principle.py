# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
# class Triangle:
#     def __init__(self, height, bottom):
#         self.height = height
#         self.bottom = bottom
#
# def calculate_area(shapes):
#     area = 0
#     for shape in shapes:
#         if isinstance(shape, Rectangle):
#             area += shape.height * shape.width
#         elif isinstance(shape, Triangle):
#             area += shape.bottom * shape.height * 0.5
#
# calculate_area(Triangle(1,2), Rectangle(2, 4))


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, height, bottom):
        self.height = height
        self.bottom = bottom

    def area(self):
        return self.height * self.bottom * 0.5



def calculate_area(shapes):
    area = 0
    for shape in shapes:
        area += shape.area()
    return area

calculate_area(Triangle(1,2), Rectangle(2, 4))
