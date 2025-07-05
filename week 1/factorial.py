p = (input('Enter an number'))
if p.isnumeric() == True:
    p = int(p)
    fac =1
    for i in range(p, 0,-1):
        fac *=i
    print(fac)
else:
    print("it is not number")
