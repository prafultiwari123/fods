def fac( p:int):
    fact = 1
    for i in range(p , 0, -1):
        
        fact *= i
    
    print(fact)

fac(5)
