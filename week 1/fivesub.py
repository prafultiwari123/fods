p = int(input("Enter math subject"))
q = int(input("Enter science subject"))
r = int(input("Enter opt math subject"))
s = int(input("Enter social subject"))
t = int(input("Enter nepali subject"))

average = (p + q + r + s + t)/5
total = p + q + r + s + t
percent = ((p + q + r + s + t)/500) * 100

if percent >=80:
    print("Distinction")
elif percent >=60:
    print("first division")
elif percent>= 50:
    print("second division")
elif percent>= 45:
    print("Third division")
else:
    print("Fail")