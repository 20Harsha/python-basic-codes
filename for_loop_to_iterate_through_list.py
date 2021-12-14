#Using for loop to check each of the elements of the list
#We are printing those numbers which are of integer datatype and greater than equal to 6
#If strings are there then it will display that these are strings.
list1 = [2,4,3,1,6,3,7,9,10,"hello",23,45,3,"mona",67,34]
l=[]
for x in list1:
    if type(x)== int:
        if x >=6 :
            l.append(x)
            print('numbers greater than equal to 6',l)
    else:
        print("These are strings : ",x)

