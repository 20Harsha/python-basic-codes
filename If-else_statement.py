#to find whether you are eligible to drive or not
age = int(input("Enter your age : "))
if age > 18 and age<100:
    print("You can drive")
elif age == 18:
    print("you have to visit center then we can decide whether you are eligible or not")
elif age>=100:
    print("Enter a valid age")
else:
    print("You are not eligible because your age is less than 18")