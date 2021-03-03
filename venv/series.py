# 1+2+3+4+.......+n

n= int(input("Enter the last number of the series:"))
sum=0
for x in range(1,n+1,1):
    sum+=x
    print(f"{sum} +",end=" ")
# print(sum)