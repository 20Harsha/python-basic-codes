print("Calculate square and cube for the number you want ")
while True:
    def sq():
        p = n * n
        print("square of : ", n, "is", p)
    def cub():
        p = n * n * n
        print("cube of :", n, "is", p)
    def both():
        p = n * n
        p1 = n * n * n
        print("\nsquare of : ", n, "is", p)
        print("cube of : ", n, "is", p1)

    b = input("\nDo you want to calculate yes or no:")
    if b=="yes":
        print("What do want to calculate square or cube or both")
        a = input("To calculate square type 0, for cube type 1 and for both type 2 : ")
        if a=="0":
            n = int(input("\nenter a number for which you want to calculate : "))
            sq()
        elif a=="1":
            n = int(input("\nenter a number for which you want to calculate : "))
            cub()
        elif a=="2":
            n = int(input("\nenter a number for which you want to calculate : "))
            both()
        else:
            print("invalid input try again")
    elif b=="no":
        print("OK! Thank you")
        break
    else:
        print("invalid input try again")



