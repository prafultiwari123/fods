p = int(input('Enter first number'))
q = int(input("Enter second number"))

while p<=q:
    if p>1:
        is_prime = True
        for i in range (2,int((p**0.5) +1)):
        
            if p % i == 0 : 
                is_prime = False
                break
        if is_prime:
            print(p)
            
            

    p +=1
