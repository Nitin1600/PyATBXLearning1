import os

full_path_file = os.path.join("/Users/nitingpa/PycharmProjects/PyATB4XLearning1/src/September/ex_10092024/Nitin", "Nitin.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)