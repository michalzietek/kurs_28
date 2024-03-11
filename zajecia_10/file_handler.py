import csv

class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.matrix = self.load_data_from_input_file()

    def load_data_from_input_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_line = []
                for number in line:
                    temp_line.append(int(number))
                temp_matrix.append(temp_line)
        return temp_matrix

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            operation = transformation_list[0]
            vector_type = transformation_list[1]
            index = int(transformation_list[2])
            value = int(transformation_list[3])
            if operation == "add" and vector_type == "row":
                self.add_row(index, value)
            elif operation == "add" and vector_type == "col":
                self.add_col(index, value)
            elif operation == "mult" and vector_type == "row":
                self.mult_row(index, value)
            elif operation == "mult" and vector_type == "row":
                self.mult_col(index, value)


    def add_col(self, index, value):
        for row in self.matrix:
            row[index] += value

    def add_row(self, index, value):
        for position, number in enumerate(self.matrix[index]):
            self.matrix[index][position] += value

    def mult_row(self, index, value):
        for position, number in enumerate(self.matrix[index]):
            self.matrix[index][number] = number * value

    def mult_col(self, index, value):
        for row in self.matrix:
            row[index] *= value
