def sum_three(a=1, b=2, c=3):
    return a + b + c

result1 = sum_three()
result2 = sum_three(10, 20)
result3 = sum_three(10,20,30)
result4 = sum_three(10)
result5 = sum_three(c=2, b=66, a=5)
result6 = sum_three(b=88)
# result7 = sum_three(b=22, c=33, a=11, 134)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
# print(result7)