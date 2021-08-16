#User will enter the number
#If the number entered by user is greater than 10 then it will break the loop
#If the number is not greater than 10 then it will continue the loop

while True:
    n = int(input("Enter the number : "))
    if n > 10:
        print("Congrats you entered number greater than 10")
        break
    else:
        print("Try again")
        continue