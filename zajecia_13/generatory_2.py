def read_data_from_file(file):
    with open(file) as opened_file:
        data = opened_file.readlines()
        for line in data:
            if line == "aaa":
                print("mamy cie")
        return data

file_data = read_data_from_file("testowy_pliczek.txt")
print(file_data)

def read_data_from_file_generator(file):
    with open(file) as opened_file:
        for line in opened_file:
            yield line

file_data_generator = read_data_from_file_generator("testowy_pliczek.txt")
for line in file_data_generator:
    print(line)