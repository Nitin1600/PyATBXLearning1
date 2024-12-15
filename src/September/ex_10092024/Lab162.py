try:
    with open("Testdata.txt1", 'r') as file:
        content = file.readlines()
    print(content)
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    try:
        file.close()
    except NameError as ne:
        print("NE")


# try:
#     with open("TestData.txt1", "r") as file:
#         content = file.readlines()
#         print(content)
# except FileNotFoundError as fnfr:
#     print(fnfr)
# finally:
#     try:
#         file.close()
#     except NameError as ne:
#         print("NE")