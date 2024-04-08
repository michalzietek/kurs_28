from abc import ABC, abstractmethod
import pickle


class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = None

    @abstractmethod
    def read_data_from_input_file(self):
        pass

    @abstractmethod
    def write_data_to_output_file(self):
        pass

    def do_changes(self):
        for change in self.changes:
            y_position, x_position, value = change.split(",")
            self.data[int(y_position)][int(x_position)] = value


class PickleFileHandler(FileHandler):
    def read_data_from_input_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def write_data_to_output_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.data, file)


class TXTFileHandler(FileHandler):
    def read_data_from_input_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            for line in file:
                temporary_data.append(line.split(","))
            self.data = temporary_data

    def write_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            file.write(self.data)