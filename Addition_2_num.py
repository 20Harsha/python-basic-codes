#addition of 2 numbers

"""using input() function to take input from user
input() function stores values in string data type
for example user enter 2 it will stored as "2" in string format
we will print those two numbers
"+" sign is used to concatenate the numbers but as numbers are in string format we convert them
in integer format using int()
"""
n1 = input("enter first number : ")
n2 = input("enter second number : ")
print("First number : ",n1)
print("Second number : ",n2)
print("Addition of two numbers is : ",int(n1) + int(n2))