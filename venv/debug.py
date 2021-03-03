#xargs(tuples)
def sum(*numbers):
    s=0
    for num in numbers:
        s=s+num
    return s
print(sum(10,20))
