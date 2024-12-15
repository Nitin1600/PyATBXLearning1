import os
try:
    file_path = os.getcwd()
    full_path_file = file_path + "/example.txt"
    print(full_path_file)

    file = open(full_path_file, 'r')
    print(file.read())
except Exception as fnfe:
    print("FIle not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)