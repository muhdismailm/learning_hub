#Electricity bill
# while(True):
#     bill=0
#     unit=int(input("Enter the unit: "))
#     if unit<=100:
#         bill =unit*5
#     elif unit>100 and unit<=200:
#         bill = (100*5)+((unit-100)*10)
#     elif unit>200:
#         bill = (100*5)+(100*10)+((unit-200)*15)
#     print("bill=",bill)
    
    
#salary bonus

# exp=int(input("Enter the experince:"))
# sal=int(input("enter the salary"))


# if exp<=3:
#     print("Your salary is :",sal)
# elif exp>3 and exp<=5:
#     sal=sal+(sal*(5/100))
# elif exp>5 and exp<=10:
#     sal=sal+(sal*(10/100))
# elif exp>10:
#     sal=sal+(sal*(15/100))
# print("your expected salary is ",sal)


#grade

# mark=int(input("Enter the mark out of 100:"))

# if mark>=95:
#     print("your grade is A+")
# elif mark>=90:
#     print("you grade is A")
# elif mark>=85:
#     print("you grade is B+")
# elif mark>=80:
#     print("you grade is B")
# elif mark>=75:
#     print("you grade is C+")
# elif mark>=70:
#     print("you grade is C")
# else:
#     print("you are failed")


# Area and perimeter
# while(True):
#     print("Enter the shape number")
#     print("1 . Square")
#     print("2. Rectangle")
#     print("3. Circle")
#     num=int(input())

#     if num==1:
#         print("Enter side of Square (in cm)\n")
#         len=int(input("enter the length"))
#         print("Area = ",(len*len))
#         print("Perimeter= ",(4*len))
#     elif num==2:
#         print("Enter length and breadth")
#         len=int(input("lenght"))
#         bre=int(input("breadth"))
#         print("Area = ",(len*bre))
#         print("Perimeter=",(2*(len+bre)))
#     elif num==3:
#         print("Enter the radius of circle")
#         rad=int(input("radius:"))
#         print("Area =",(3.14*rad**2))
#         print("Circumference",(2*3.14*rad))
#     else :
#         print("provide proper number!")

#prime number
num=int(input("enter a number"))
for i in range(2,int(num*0.5)+1):
    prime=True
    if num%i==0:
        prime=False
    break

if prime:
    print("it is a prime number")
else:
    print("not a prime")
    
    