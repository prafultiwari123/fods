import random
p = random.randint(0, 100)
q = True
count = 0
while q:

    r = int(input("Please enter a number"))
    count += 1
    if count<=4:
        if r ==p:
            print("You win")
            q = False
        elif r<p:
             print("it is smaller than p")
        elif r>p:
            print("The number is bigger")
        print("guessed ",count)
    else: 
        print("you lose")
        q = False
print("The number was", p)