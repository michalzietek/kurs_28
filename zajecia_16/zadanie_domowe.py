from file_handler import PickleFileHandler, TXTFileHandler
import sys


def load_arguments():
    return sys.argv[1], sys.argv[2], sys.argv[3:]

input_file, output_file, changes = load_arguments()

if input_file.endswith(".txt"):
    input_file_handler = TXTFileHandler(input_file, output_file, changes)
elif input_file.endswith(".pkl"):
    input_file_handler = PickleFileHandler(input_file, output_file, changes)
else:
    print("nie mamy takiego pliku")

if output_file.endswith(".txt"):
    output_file_handler = TXTFileHandler(input_file, output_file, changes)
elif output_file.endswith(".pkl"):
    output_file_handler = PickleFileHandler(input_file, output_file, changes)
else:
    print("nie mamy takiego pliku")

input_file_handler.read_data_from_input_file()
input_file_handler.do_changes()
output_file_handler.data = input_file_handler.data
output_file_handler.write_data_to_output_file()


