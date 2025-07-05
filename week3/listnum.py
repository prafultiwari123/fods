def listnum():
    lister = True
    liste= []
    while lister == True:
        s =int(input("Add a number:"))
        p =input("do you want to continue")
        if p=="yes":
            lister = True
            liste.append(s)
        else:
            lister = False
            liste.append(s)

    print(liste)

    for i in range(len(liste)):
        print(i, "=" ,liste[i])


listnum()