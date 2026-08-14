# def prt():
#     for x in range(1,11):
#         print(x)

# print("number upto 10")
# prt()

# def area(x,y):
#     ar=x*y
#     print("Area of rectangle = ",ar)

# a=int(input("length = "))
# b=int(input("breadth ="))

# area(a,b)

# def large(a,b,c):
#     if a>b and a>c:
#         print("largest=",a)
#     elif b>a and b>c:
#         print("largest=",b)
#     else:
#         print("largest=",c)
        
# print("enter three numbers")
# x=int(input())
# y=int(input())
# z=int(input())

# large(x,y,z)

# def greet(name,msg="Good Morning"):
#     print(msg,name+"!")

# x=input("Type your name")
# greet(x)

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student(name="Ismail", age=22)
# def largest(*args):
#     large=args[0]
#     for i in args:
#         if i >large:
#             large=i
#     return large

# print(largest(10, 25, 7, 42, 18))


def details(**kwargs):
    print("Details:",kwargs)
    
details(name="Ismail", age=22, city="New York")