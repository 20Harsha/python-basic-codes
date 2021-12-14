#User will enter the number
#loop continues until the number entered is less than 10 using continue statement
#loop breaks when number entered is greater than 10

while True:
    n = int(input("Enter the number : "))
    if n > 10:
        print("Congrats you entered number greater than 10")
        break
    else:
        print("Try again")
        continue
