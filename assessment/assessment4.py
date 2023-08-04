x1=int(input("Enter the day"))
x2=int(input("Enter the month"))
x3=int(input("Enter the year"))
if(x3/4==0 and x3/100!=0):
    print("this year is a leap year")
else:
    print("this year is not a leap year")

if(3<=x2<=5):
    print("spring")
elif(6<=x2<=8):
    print("Summer")
elif(9<=x2<=11):
    print("autumn")
else:
    print("winter")