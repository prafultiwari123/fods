l =["kathmandu","london", "New york" ]

def search():
    print(l)

    p = input("Enter the cities you wanrt to search")

    for i in range(len(l)):
        if p == l[i]:
            print(i)
            return i
        
    print("City is not found")

search()