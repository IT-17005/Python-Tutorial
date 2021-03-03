s = input("Enter the Text:")
numOfDigit=0
numOfletter=0
numOfWord=0
for i in s:
    i=i.lower()
    if i>='a' and i<='z':
        numOfletter+=1

    elif i>='0' and i<='9':
        numOfDigit+=1

    elif i==' ':
        numOfWord+=1

print("The number of words:",numOfWord+1)
print("The number of letters:",numOfletter)
print("The number of Digit:",numOfDigit)