n = input("Enter a text of number:")#12 12 32 43 54
list = n.split()#12, 12, 32, 43
sum=0
for num in list:
    sum+=int(num)
print(sum)