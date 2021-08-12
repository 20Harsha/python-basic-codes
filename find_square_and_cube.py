#find square of a number by taking input from user

"""
Using input() function we take input from user
As the input will be in string format so to convert it to int datatype we use int()
So when user enter : 2 ,input() function will take as "2" as string but then int() converts it to 2 that is integer format
we assign 2 different variables a and b to calculate square and cube
print our results but as our a and b are integer format so to concatenate it with string
we have to convert it to string format for that we use str()
we can see type by using type() function
eg:print(type(a))  will return us the type of a
"""
num = int(input("Enter the number : "))
a = num ** 2   #calculating square
b = num ** 3   #calculating cube
print("Square of "+str(num)+" is "+str(a))
print("Cube of " + str(num)+" is "+str(b))