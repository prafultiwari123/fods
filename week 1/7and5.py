p = int(input('Enter a number'))
q = int(input("Enter bigger number"))


for i in range (p, q +1):
    if i % 7 ==0 and i % 5 !=0:
        print(i)
        