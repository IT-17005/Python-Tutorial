# map(function, list)
def square(x):
    return x*x

num = [1,2,3,4,5,6,7]
result = list(map(square,num))
print(result)