#Swapping two numbers

while True:
    user = input("\nDo you want to Swap 2 numbers 'y' or 'n'? : ")
    if user == 'y':
        num1 = int(input("Enter first number : "))  #entering first number
        num2 = int(input("Enter second number : ")) #entering second number
        print(f"\nNum1 : {num1} , Num2 : {num2}")  #Using f-strings to print numbers
        num1,num2 = num2,num1   #Swapping two numbers
        print("\nSwapped numbers")
        print(f"Num1 : {num1} , Num2 : {num2}")

    else:
        print("Goodbye")
        break
