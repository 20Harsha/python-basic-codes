#Calculator performing simple operations like addition, multiplication, subtraction and division.
while True:
    a = input("\nDo you want to calculate something 'yes' or 'no' : ")
    if a=="yes":
        n = int(input("Enter first number : "))
        m = int(input("Enter second number : "))
        while True:
            a="""
              ------------------------------------------------
              |    (+) for Addition     | (-) for Subtraction |
              |  (*) for Multiplication |  (/) for Division   |
              -------------------------------------------------
            """
            o = input(f"Enter operator \n{a}\n: ")
            if o == "*":
                print(f"{n} * {m} = {n*m}")
                break
            elif o == "+":
                print(f"{n} + {m} = {n + m}")
                break
            elif o == "/":
                if m==0:
                    print("Zero division Error")
                    print(f"{n} / 0 !!Not possible")
                else:
                    print(f"{n} / {m} = {n / m}")
                break
            elif o == "-":
                print(f"{n} - {m} = {n - m}")
                break
            else:
                print("Not available")
                break
    else:
        break

