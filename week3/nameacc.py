def name():
    s = int(input("How many name do you want to accept"))
    b = []
    for i in range(s):
        p = input("Enter the name ")
        b.append(p)
    b.sort()
    print(b)
name()
