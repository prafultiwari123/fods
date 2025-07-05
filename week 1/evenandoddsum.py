p = True
sum = 0
while p:
    
    q = int(input("please enter a number"))
    sum +=q
    print(sum)
    r = (input("Do you want to continue")) 
    if r == "False":
        p = False