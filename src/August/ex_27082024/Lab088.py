# def sum_three_num(a,b,c):
#     return a + b + c
#
# op = lambda a,b,c: a + b + c
# print(op(322,112,4545))

def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))