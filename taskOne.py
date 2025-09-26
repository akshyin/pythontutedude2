#Take an indicator for error happened in input
errorfound=False
#Take the number as input from user and assign it to number variable
number=input("Enter the integer: ")
#Convert number into integer
try:
    number=int(number)
except ValueError:
    errorfound=True
    print("Error in reading number")

if not errorfound:
    if(number%2==0):
        print(number," is even number")
    else:
        print(number," is odd number")
