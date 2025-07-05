p = int(input("Enter first number for a"))
q = int(input("Enter second number for b"))
r = int(input("Enter third number for c"))

f = p**2 + 2*p*q + q**2
g = p**5 + 2 * p *q * r + q ** 3 + r ** 4
h = p ** 7 + 5*p**3 *q**2 * r**6 + r ** 7

print("For expression 1", f)
print("for expression 2", g)
print('for expression 3', h)