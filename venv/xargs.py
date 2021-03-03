#xargs(tuples)
def sum(*numbers):
    s=0
    for num in numbers:
        s=s+num
    print(s)

sum(10,20)
sum(10,20,45)
sum(10,20,68)