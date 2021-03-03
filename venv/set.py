num1 = {1,2,3,4,5,6}
num2 = set([1,2,38,9])
num1.add(11)
num1.remove(11)
print(11 not in num1)
print(num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)